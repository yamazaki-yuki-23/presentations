# WebMCP とは何か、なぜ広がるのか

2026-11-16 の社内勉強会の資料。全 32 枚、5 章構成。

- スライド本体（Claude の Slides Artifact）: <https://claude.ai/artifact/4xKAhLvk4H3KLM6q5hpTNi>
- デモ: <https://github.com/yamazaki-yuki-23/webmcp-demo>
- 6 枚目の動画: Chrome for Developers「What is WebMCP?」 <https://www.youtube.com/watch?v=NERX01dOiEY>

## このフォルダの中身

このリポジトリのほかの資料と違い、Marp ではなく Claude の Slides Artifact で作っている。
そのため `slides.md` はなく、`build:*:all` と Pages のワークフローの対象にならない。
ソースは Artifact 側にあり、ここには表示用の書き出しだけを置く。

- `slides.html`: Artifact のページから書き出した単体の HTML（⬇ → Web page (.html)）。ブラウザで開く。本文と話す原稿を含む

生成物を Git に含めない決まりの例外として、この資料だけ `slides.html` を含めている。
6 枚目の動画の埋め込みは書き出しでは黒い枠になる。動画は上の URL から開く。

## デザインの決まり

大木尊紀氏「『見せる』登壇資料デザインの極意」（<https://youtu.be/rIueuWNfcCQ>）に従う。
タイトルで結論を言う、箇条書きとカードを使わない、1 枚 5 行以内、白地・2 色・左揃え、
本文 48px、出典は最後の 1 枚にまとめる、各章の前に区切りページ。
