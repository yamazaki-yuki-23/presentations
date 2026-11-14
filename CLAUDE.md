# CLAUDE.md

登壇・勉強会のスライドを置くリポジトリ。スライドは Claude の Slides Artifact で作る。
Marp は 2026-11 でやめた（`2026/ts-6.0`、`2026/temporal-api`、`2026/nextjs-router-cache-bug` は
Marp 時代の資料で、そのまま残している。ビルドの道具は消したので、要るときは
`npx @marp-team/marp-cli` で単発に変換する）。

## 必須ルール

- スライドを作る・直すときは `/slides` スキル（`.claude/skills/slides/SKILL.md`）の手順どおりに進める。
  構成、デザインの決まり、文面の検査（yomiyasu）、画面での確認、置き方までそこにある
- 雛形は `templates/`（`deck.json`、`deck.css`、`slides/*.html`）。deck.css は変えずに使い、
  足りない部品だけ末尾に足す
- 公開の前に `python3 scripts/check-deck.py <作業フォルダ>/project` をエラー 0 にする
- Artifact に公開する前に、必ず `action: "read"` で相手の最新版を読む（オーナーがページ側で直す）
- 公開前提なので、機密情報・社内限定の値を入れない。非公開のメモは各発表の `.private/` に置く
- 新しい依存を足さない。スクリプトは Python 3 の標準ライブラリだけで書く

## 置き場

```text
<year>/<kebab-topic>/
├─ README.md     # 題、日付、場、Artifact の URL、デモや動画の URL
└─ slides.html   # Artifact のページから書き出した単体の HTML（⬇ → Web page (.html)）
```

ソース（deck.json・deck.css・slides）は Artifact 側にあるので置かない。
`slides.html` は生成物だが、リポジトリで開ける唯一の形なので含める。

## コマンド

```bash
python3 scripts/check-deck.py <deck>/project   # デザインの決まりの検査（終了コード 1 でエラーあり）
python3 scripts/check-deck.py --selftest       # 検査の自己テスト
npx markdownlint-cli2 "**/*.md"                # README の体裁
```

## 出力スタイル

読み手は ADHD。答えや次の行動から始め、複数ステップは番号を付け、1 ステップに行動 1 つ。
2 分以内にできる次の行動を 1 つ示して終える。前置き・要約・締めの挨拶は入れない。
破壊的操作の前には確認を取る。指示が曖昧なら短い質問を 1 つだけする。
