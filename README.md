# 発表資料リポジトリ（Marp）

このリポジトリは、Marp を使って Markdown で作成した技術発表スライドを管理するためのものです。

このリポジトリの目的は次のとおりです。

- スライドのソースを Markdown で管理する
- 生成物（PDF / HTML）を Git に含めない
- 年度とトピック単位で発表資料を整理する
- 再現可能でバージョン管理しやすい構成にする

---

## リポジトリ構成

```text
.
├─ .gitignore
├─ 2026/
│   └─ ts-6.0/
│       ├─ slides.md
│       ├─ README.md
│       └─ assets/
│
├─ templates/
│   ├─ base.md
│   └─ theme.css
│
├─ assets/
│   └─ images/
│
├─ dist/              # 生成物（git管理しない）
├─ LICENSE
├─ package.json
├─ bun.lock
├─ bun.lockb
└─ README.md
```

---

## 方針

- スライド本文は Markdown で作成する
- 生成物は Git で追跡しない
- 発表ごとに独立したディレクトリを持つ
- 共通テーマやスタイルは `templates/` で管理する
- 公開前提で管理し、機密情報や社内限定資料は含めない

---

## セットアップ

依存関係をインストールします。

```bash
bun install
```

VS Code を利用する場合は、拡張機能 `Marp for VS Code` の導入を推奨します。

---

## スライドのプレビュー

```bash
bun run preview
```

ローカルのプレビューサーバーが起動し、`2026/ts-6.0/slides.md` を監視します。

## Mintlify ドキュメントのプレビュー

Mintlify 用の設定は `docs.json` と `docs/` 配下にあります。

公式ドキュメントでは、`docs.json` のあるディレクトリで `mint dev`、または一時実行として `npx mint dev` が案内されています。

```bash
bun run docs:dev
```

初回実行時に `npx` 経由で Mintlify CLI を取得します。

---

## スライドの生成

### HTMLを生成

```bash
bun run build:html 2026/ts-6.0/slides.md
```

### PDFを生成

```bash
bun run build:pdf 2026/ts-6.0/slides.md
```

指定した `slides.md` は、`dist/` 配下に元のディレクトリ構造を保って出力されます。

```text
2026/ts-6.0/slides.md
-> dist/2026/ts-6.0/slides.pdf
```

### すべてのスライドをPDF生成

```bash
bun run build:pdf:all
```

### すべてのスライドをHTML生成

```bash
bun run build:html:all
```

生成物は `dist/` 配下に出力されます。

---

## GitHub Actions で手動生成

GitHub の `Actions` から `Render Slides` workflow を手動実行できます。

- `slide_path`: 例 `2026/ts-6.0/slides.md`
- `output`: `pdf` / `pages` / `both`

### `pdf`

指定した資料を PDF に変換し、artifact として保存します。

### `pages`

指定した資料だけを HTML として GitHub Pages に公開します。  
毎回 1 資料ずつ上書き公開する運用です。

### `both`

PDF artifact と GitHub Pages 公開の両方を行います。

---

## 新しい発表資料を追加する手順

1. 対象年度の配下に新しいディレクトリを作成する
2. `templates/base.md` をベースに `slides.md` を作成する
3. 画像は各発表ディレクトリの `assets/` 配下に配置する
4. 上記スクリプトでプレビューと生成を行う

---

## ライセンス

MIT
