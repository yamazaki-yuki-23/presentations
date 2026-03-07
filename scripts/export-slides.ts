import { spawnSync } from "node:child_process";
import { mkdirSync } from "node:fs";
import { dirname, isAbsolute, relative, resolve } from "node:path";

type Format = "pdf" | "html";

const projectRoot = process.cwd();
const distRoot = resolve(projectRoot, "dist");
const themePath = resolve(projectRoot, "templates/theme.css");
const marpBin = resolve(projectRoot, "node_modules/.bin/marp");

function usage(): void {
  console.error("Usage: bun run build:pdf <path/to/slides.md>");
  console.error("   or: bun run build:html <path/to/slides.md>");
  console.error("   or: bun run build:pdf:all / build:html:all");
}

function assertInsideRepo(filePath: string): string {
  const rel = relative(projectRoot, filePath);
  if (rel.startsWith("..")) {
    throw new Error(`Input must be inside repository: ${filePath}`);
  }
  return rel;
}

function outputExtension(format: Format): string {
  return format === "pdf" ? ".pdf" : ".html";
}

function buildOutputPath(inputPath: string, format: Format): string {
  const relativeInput = assertInsideRepo(inputPath);
  return resolve(distRoot, relativeInput.replace(/\.md$/i, outputExtension(format)));
}

function marpArgs(format: Format, inputPath: string, outputPath: string): string[] {
  const args = [inputPath, "--theme-set", themePath, "-o", outputPath];
  return format === "pdf" ? ["--pdf", ...args] : args;
}

function runMarp(format: Format, inputPath: string, outputPath: string): void {
  mkdirSync(dirname(outputPath), { recursive: true });

  const result = spawnSync(marpBin, marpArgs(format, inputPath, outputPath), {
    stdio: "inherit",
  });

  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }

  const relativeOutput = relative(projectRoot, outputPath);
  console.log(`Generated ${relativeOutput}`);
}

function findSlideFiles(): string[] {
  const result = spawnSync(
    "find",
    [
      projectRoot,
      "-type",
      "f",
      "-name",
      "slides.md",
      "-not",
      "-path",
      "*/node_modules/*",
      "-not",
      "-path",
      "*/dist/*",
    ],
    { encoding: "utf8" },
  );

  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }

  return result.stdout
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean)
    .sort();
}

const args = process.argv.slice(2);
const format = args[0] as Format | undefined;
const restArgs = args.slice(1);

if (!format || !["pdf", "html"].includes(format)) {
  usage();
  process.exit(1);
}

if (restArgs.length === 1 && restArgs[0] === "--all") {
  const slideFiles = findSlideFiles();

  if (slideFiles.length === 0) {
    console.error("No slides.md files found.");
    process.exit(1);
  }

  for (const slideFile of slideFiles) {
    runMarp(format, slideFile, buildOutputPath(slideFile, format));
  }

  process.exit(0);
}

const inputArg = restArgs[0];

if (!inputArg || restArgs.length > 1) {
  usage();
  process.exit(1);
}

const inputPath = isAbsolute(inputArg) ? inputArg : resolve(projectRoot, inputArg);
runMarp(format, inputPath, buildOutputPath(inputPath, format));
