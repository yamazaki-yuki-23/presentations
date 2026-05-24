# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

Marp ベースの技術発表スライドを Markdown で管理するリポジトリ。生成物 (PDF / HTML) は Git に含めず、年度 × トピック単位でディレクトリを切る。スライドは公開前提なので、機密情報を入れない。

## Commands

Bun ベース。`package.json` のスクリプトを直接叩く。

- `bun install` — 依存インストール（`@marp-team/marp-cli` のみ）
- `bun run preview` — Marp のローカルサーバーを起動して `slides.md` を監視
- `bun run build:pdf <path/to/slides.md>` — 単一スライドを PDF 化
- `bun run build:html <path/to/slides.md>` — 単一スライドを HTML 化
- `bun run build:pdf:all` / `bun run build:html:all` — リポジトリ内のすべての `slides.md` を一括ビルド
- `bun run docs:dev` — Mintlify (`docs/` + `docs.json`) のローカルプレビュー（`npx mint dev` 経由）

テストや lint は未設定。markdownlint の設定 (`.markdownlint.jsonc`) のみ存在。

## Architecture

3 つの独立した成果物を 1 リポジトリで管理している。これらは互いに依存しない。

1. **Marp スライド** — `<year>/<topic>/slides.md`。各発表ディレクトリに `README.md` と `assets/` を同梱する。テーマは `templates/theme.css`（`@theme blueprint`、Gaia 拡張）、雛形は `templates/base.md`。
2. **Mintlify ドキュメント** — `docs.json` + `docs/*.mdx`。リポジトリの使い方を説明する公開ドキュメントで、スライド本体とは別物。
3. **エクスポートスクリプト** — `scripts/export-slides.ts`（Bun 実行）。`build:*` スクリプトの実体。

### `scripts/export-slides.ts` の挙動

- 入力パスはリポジトリ外を拒否し、`dist/` 配下に**元のディレクトリ構造を保ったまま**出力する（例: `2026/ts-6.0/slides.md` → `dist/2026/ts-6.0/slides.pdf`）。
- `--all` モードは `find` で `slides.md` を再帰検索する（`node_modules` と `dist` を除外）。新しい発表を追加する際にファイル名を `slides.md` 以外にすると `:all` ビルドから漏れる点に注意。
- Marp バイナリは `node_modules/.bin/marp` を直接呼び出し、テーマは常に `templates/theme.css` を `--theme-set` で渡す。

### GitHub Actions (`.github/workflows/render-slides.yml`)

`workflow_dispatch` のみ。手動で `slide_path` と `output` (`pdf` / `pages` / `both`) を指定する。

- `pdf` ジョブ: PDF を artifact としてアップロード。
- `pages` ジョブ: HTML を `.pages/` に配置して GitHub Pages にデプロイ。**毎回 1 資料ずつ上書き公開**する運用（過去資料は残らない）。トップに `slide_path` へのリダイレクト用 `index.html` を生成する。
- 両ジョブとも CJK / IBM Plex フォントを apt で入れてからビルドする。日本語スライドの PDF レンダリングはこのフォント導入に依存する。

## Conventions

- 新しい発表は `<year>/<kebab-topic>/` を作り、`templates/base.md` をコピーして `slides.md` を作る。画像は同ディレクトリの `assets/` に置く（`build:*:all` と Pages ワークフローはこの構造を前提にしている）。
- 共通テーマ・スタイルは `templates/` に集約する。個別スライドの `style:` フロントマターは最小限に。
- `dist/` は `.gitignore` 済み。生成物をコミットしない。
- `**/.private/` も `.gitignore` 済み。下書きや非公開メモは各発表配下の `.private/` に置けば除外される。

## Agent skills (APM)

エージェント向けスキルは [APM (Agent Package Manager)](https://github.com/microsoft/apm) で管理する。modern mode（`--legacy-skill-paths` を付けない）で運用しており、cross-client 共通パスに配備する。

- **Source of truth**: `.apm/skills/<name>/SKILL.md`（`apm.yml` / `apm.lock.yaml` も git 管理）。
- **Generated** (gitignore 済み、`apm install` で再生成):
  - `.agents/skills/` — APM が定める cross-client 共通パス。Codex / Copilot など `apm.yml` の `targets:` に並ぶエージェントはここを参照する想定。
  - `.claude/skills/` — Claude Code 専用パス。Claude Code は起動時にここを読む。
- 配布先のターゲットは `apm.yml` の `targets:` で制御（現在は `claude`, `copilot`, `codex`）。スキルを追加・編集したら `apm install` を実行し、利用するエージェントを再起動する。
