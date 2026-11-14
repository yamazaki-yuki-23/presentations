# 発表資料リポジトリ

登壇・勉強会のスライドを年度とトピック単位で置く。スライドは Claude の Slides Artifact で作り、
ここには書き出した HTML と README を置く。

## 構成

```text
.
├─ 2026/
│   └─ webmcp/
│       ├─ README.md      # 題、日付、場、Artifact の URL
│       └─ slides.html    # Artifact から書き出した単体の HTML
├─ templates/
│   ├─ deck.json          # 枚の順番と章の雛形
│   ├─ deck.css           # 共通のスタイル（白地、紺と橙の 2 色）
│   └─ slides/*.html      # 枚の型（表紙、目次、章の区切り、列挙、2 列、表、流れ、時系列、図、動画、コード、おわり、出典）
├─ scripts/check-deck.py  # デザインの決まりの検査
└─ .claude/skills/slides/ # 作り方の手順
```

## 新しい資料を作る

1. Claude Code でこのリポジトリを開き、`/slides` に発表の日付・場・聴衆・持ち時間・伝えたいことを渡す
2. Artifact 上で 1 枚ずつ確かめ、文面は yomiyasu、形は `scripts/check-deck.py` で検査する
3. 仕上がったら Artifact のページの ⬇ → Web page (.html) で書き出し、`<year>/<topic>/slides.html` に置く
4. `<year>/<topic>/README.md` に題、日付、場、Artifact の URL を書く

## 決まり

- 大木尊紀氏「『見せる』登壇資料デザインの極意」（<https://youtu.be/rIueuWNfcCQ>）に従う。
  題で結論を言う、箇条書きとカードを使わない、1 枚 5 行まで、白地・2 色（白地で 9:1 以上）・左揃え、
  本文 48px、出典は最後の 1 枚にまとめる、各章の前に区切りの枚
- 公開前提。機密情報を入れない。非公開のメモは各発表の `.private/` に置く（Git には入らない）

## Marp 時代の資料

`2026/ts-6.0`、`2026/temporal-api`、`2026/nextjs-router-cache-bug` は Marp で作った。
ビルドの道具は消したので、変換が要るときは単発で実行する。

```bash
npx @marp-team/marp-cli 2026/ts-6.0/slides.md -o /tmp/ts-6.0.pdf
```

## ライセンス

MIT
