---
marp: true
theme: blueprint
paginate: true
size: 16:9
style: |
  section {
    font-size: 24px;
    padding: 56px 72px;
  }
  section::before { display: none; }
  section h1 {
    font-size: 40px;
    border-left: none;
    padding-left: 0;
    margin: 0 0 6px;
  }
  section h2 {
    font-size: 20px;
    color: #6b7a8f;
    font-weight: 400;
    margin: 0 0 30px;
  }
  section.lead {
    text-align: left;
    justify-content: center;
    align-items: flex-start;
    padding: 96px 104px;
    background-image:
      linear-gradient(135deg, #0a1538 0%, #1e3a73 55%, #2a5f9e 100%);
    color: #fff;
  }
  section.lead::before { display: none; }
  section.lead h1 {
    color: #fff;
    font-size: 92px;
    font-weight: 800;
    line-height: 1.25;
    text-align: left;
    margin-bottom: 20px;
    letter-spacing: 0;
  }
  section.lead h2 {
    color: #cfd8e8;
    font-size: 28px;
    font-weight: 400;
    margin-bottom: 0;
    text-align: left;
  }
  .lead-strip {
    display: flex;
    align-items: center;
    gap: 36px;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 18px;
    padding: 28px 44px;
    width: 100%;
    margin-top: 24px;
  }
  .lead-strip .big-number {
    font-size: 104px;
    font-weight: 800;
    color: #ffcc66;
    line-height: 0.9;
  }
  .lead-strip .strong {
    font-weight: 700;
    font-size: 30px;
    color: #fff;
  }
  .lead-strip .sub {
    color: #cfd8e8;
    font-size: 19px;
    margin-top: 8px;
    letter-spacing: 0.04em;
  }
  .lead-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 16px;
    padding: 22px 26px;
  }
  .lead-card .meta {
    color: #aab9d4;
    font-size: 14px;
    letter-spacing: 0.06em;
    margin-bottom: 10px;
  }
  .lead-card .desc {
    color: #ecf3ff;
    font-size: 19px;
    line-height: 1.5;
  }
  .lead-card.accent {
    display: flex;
    align-items: center;
    gap: 20px;
  }
  .big-number {
    font-size: 80px;
    font-weight: 800;
    color: #ffcc66;
    line-height: 0.9;
  }
  .lead-card.accent .strong { font-weight: 700; font-size: 22px; color: #fff; }
  .lead-card.accent .sub { color: #cfd8e8; font-size: 15px; margin-top: 4px; }
  .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1.15fr; gap: 20px; align-items: start; }
  .grid-3x2 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
  .card {
    background: #fff;
    border: 1px solid #e3eaf3;
    border-radius: 14px;
    padding: 18px 22px;
    box-shadow: 0 1px 3px rgba(15, 31, 51, 0.04);
  }
  .card .label {
    color: #1765d1;
    font-weight: 700;
    font-size: 13px;
    margin-bottom: 6px;
    letter-spacing: 0.03em;
  }
  .card h3 {
    margin: 0 0 6px;
    font-size: 22px;
    color: #0f1f33;
  }
  .card .chip {
    display: inline-block;
    background: #e7f0ff;
    color: #1765d1;
    border-radius: 999px;
    padding: 3px 12px;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 8px;
  }
  .card .desc {
    color: #4a5b73;
    font-size: 17px;
    line-height: 1.5;
  }
  .kw-bar {
    background: rgba(23, 101, 209, 0.08);
    border-left: 6px solid #1765d1;
    border-radius: 0 10px 10px 0;
    padding: 14px 20px;
    margin-top: 22px;
    font-size: 20px;
  }
  .date-figure {
    background: #e7eff8;
    border-radius: 18px;
    padding: 32px 28px;
    min-height: 360px;
  }
  .date-figure .date-title {
    font-size: 64px;
    font-weight: 800;
    color: #1765d1;
    margin-bottom: 20px;
    line-height: 1;
  }
  .date-figure .pill {
    display: inline-block;
    background: #fff;
    border: 1px solid #c5d6ea;
    border-radius: 999px;
    padding: 7px 18px;
    color: #1765d1;
    font-size: 16px;
    margin: 4px 6px 4px 0;
    font-weight: 600;
  }
  .issues { display: grid; gap: 12px; }
  .issues .card .h { font-weight: 800; font-size: 20px; color: #0f1f33; margin-bottom: 2px; }
  .issues .card .d { color: #4a5b73; font-size: 17px; }
  section.quiz h1::before {
    content: "❓  ";
    color: #f97316;
  }
  section.quiz pre {
    font-size: 22px;
    margin: 6px 0 22px;
    min-height: 0;
    border: none;
    background: #0a0f1f;
    box-shadow: 0 6px 18px rgba(15, 31, 51, 0.08);
  }
  .options {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
  }
  .option {
    background: #fff;
    border: 1.5px solid #fcd9b6;
    border-radius: 14px;
    padding: 14px 16px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
    font-size: 17px;
    line-height: 1.4;
    min-height: 76px;
  }
  .option .letter {
    background: #ffe0c2;
    color: #c84d12;
    border-radius: 50%;
    width: 32px;
    height: 32px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    flex-shrink: 0;
  }
  .hint {
    display: inline-block;
    background: #4a1f12;
    color: #ffd8b8;
    border-radius: 10px;
    padding: 10px 18px;
    margin-top: 18px;
    font-size: 17px;
  }
  .ans-badge {
    position: absolute;
    top: 56px;
    right: 72px;
    width: 60px;
    height: 60px;
    background: #2ecc71;
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 30px;
  }
  .answer-body .card h3 { color: #1765d1; font-size: 20px; }
  .answer-body pre {
    margin: 0;
    min-height: 0;
    border: none;
    box-shadow: none;
    background: #0a0f1f;
    font-size: 17px;
  }
  .answer-body .dark {
    background: #0a0f1f;
    border-radius: 14px;
    padding: 16px 20px;
  }
  .answer-body .dark h3 { color: #6db4ff; }
  .callout {
    background: rgba(23,101,209,0.08);
    border-left: 6px solid #1765d1;
    border-radius: 0 10px 10px 0;
    padding: 14px 20px;
    margin-top: 18px;
    font-size: 19px;
    font-weight: 600;
  }
  .compare table {
    font-size: 18px;
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 10px;
    overflow: hidden;
  }
  .compare th {
    background: #0a0f1f;
    color: #fff;
    text-align: left;
    padding: 14px 18px;
    font-size: 18px;
    border: none;
  }
  .compare td {
    padding: 14px 18px;
    border: none;
    border-bottom: 1px solid #e3eaf3;
    background: #fff;
  }
  .compare tr:nth-child(even) td {
    background: #f7f9fc;
  }
  .sum-list { display: grid; gap: 12px; }
  .sum-item {
    display: flex;
    align-items: center;
    gap: 18px;
    background: #fff;
    border: 1px solid #e3eaf3;
    border-radius: 12px;
    padding: 16px 22px;
    font-size: 19px;
  }
  .sum-item .num {
    background: #e7f0ff;
    color: #1765d1;
    font-weight: 800;
    border-radius: 50%;
    width: 36px;
    height: 36px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }
  .cta {
    background: #0a0f1f;
    color: #fff;
    border-radius: 12px;
    padding: 18px 22px;
    margin-top: 16px;
    font-weight: 700;
    font-size: 22px;
    text-align: center;
  }
  .ref { display: grid; gap: 10px; margin-top: 4px; }
  .ref-item {
    border-left: 4px solid #1765d1;
    padding: 6px 14px;
    font-size: 18px;
    color: #2c3e5e;
  }
  .ref-item b { color: #0f1f33; }
---

<!-- _class: lead -->

# Node.js v26 で<br>標準化された Temporal

## Date の何が問題で、Temporal が何を解決するのか

---

# 今日のゴール
## 「Date が変」ではなく「何を表したい値なのか」を言語化できる状態になる

<div class="grid-4">
<div class="card">
<h3>Date の違和感</h3>
<div class="desc">Date 1 つで多様な日時を扱うため、意味が曖昧になりやすい。</div>
</div>
<div class="card">
<h3>3 択クイズ</h3>
<div class="desc">月末加算 / 文字列パース / 不正日付の挙動を予想する。</div>
</div>
<div class="card">
<h3>Temporal の構成</h3>
<div class="desc">Instant / PlainDate / ZonedDateTime など、用途別に分けられたオブジェクト構成を押さえる。</div>
</div>
<div class="card">
<h3>使いどころ</h3>
<div class="desc">明日からどこに入れるかを決める。</div>
</div>
</div>

---

# Date は「全部入り」すぎる
## ひとつのオブジェクトに、絶対時刻・表示・成分・パース・計算が同居している

<div class="grid-2">
<div class="date-figure">
<div class="date-title">Date</div>
<span class="pill">timestamp</span>
<span class="pill">年月日時分秒</span><br>
<span class="pill">ローカル時刻</span>
<span class="pill">UTC</span><br>
<span class="pill">パース</span>
<span class="pill">変更操作</span>
<span class="pill">表示</span>
</div>
<div class="issues">
<div class="card">
<div class="h">1. ミュータブル</div>
<div class="d">setter が元のインスタンスを書き換える。</div>
</div>
<div class="card">
<div class="h">2. 意味が混ざる</div>
<div class="d">同じ値を「瞬間」とも「年月日」とも読める。</div>
</div>
<div class="card">
<div class="h">3. 暗黙のタイムゾーン</div>
<div class="d">UTC と実行環境ローカルが混ざりやすい。</div>
</div>
<div class="card">
<div class="h">4. パースが揺れる</div>
<div class="d">文字列の形で解釈が変わる。</div>
</div>
</div>
</div>

---

<!-- _class: quiz -->

# Quiz 1. 1月31日の「1ヶ月後」は？
## このコードの出力を予想してください

```js
const d = new Date("2026-01-31T00:00:00Z");
d.setUTCMonth(d.getUTCMonth() + 1);
console.log(d.toISOString());
```

<div class="options">
<div class="option"><span class="letter">A</span><span>2026-02-28T00:00:00.000Z</span></div>
<div class="option"><span class="letter">B</span><span>2026-03-03T00:00:00.000Z</span></div>
<div class="option"><span class="letter">C</span><span>TypeError</span></div>
</div>

---

# Answer 1. 正解は **B**。しかも元の値も書き換わる
## Date の setter はミュータブル。存在しない日付は黙って繰り上がる

<div class="ans-badge">B</div>

<div class="answer-body grid-2">
<div class="card">
<h3>Date で起きていること</h3>

- `setUTCMonth()` は **d 自身**を書き換える
- 2026 年 2 月 31 日は存在しない
- 結果として **3 月 3 日**にオーバーフローする

</div>
<div class="dark">

```js
const start = Temporal.ZonedDateTime.from(
  "2026-01-31T10:00[Asia/Tokyo]"
);
const next = start.add({ months: 1 });

start.toString(); // 2026-01-31T10:00...
next.toString();  // 2026-02-28T10:00...
```

</div>
</div>

<div class="callout">Temporal の変更操作は<strong>新しい値</strong>を返す。月末加算もカレンダーとして扱える。</div>

---

<!-- _class: quiz -->

# Quiz 2. ハイフンとスラッシュ、1 文字違うだけ
## Asia/Tokyo で実行した場合、出力はどうなる？

```js
console.log(new Date("2026-01-01").toISOString());
console.log(new Date("2026/01/01").toISOString());
```

<div class="options">
<div class="option"><span class="letter">A</span><span>2026-01-01T00:00:00.000Z<br>2026-01-01T00:00:00.000Z</span></div>
<div class="option"><span class="letter">B</span><span>2026-01-01T00:00:00.000Z<br>2025-12-31T15:00:00.000Z</span></div>
<div class="option"><span class="letter">C</span><span>2025-12-31T15:00:00.000Z<br>2026-01-01T00:00:00.000Z</span></div>
</div>

---

# Answer 2. 正解は **B**。文字列形式で解釈が変わる
## 日付だけを表したいのに、UTC やローカル TZ が紛れ込む

<div class="ans-badge">B</div>

<div class="answer-body grid-2">
<div class="card">
<h3>Date の落とし穴</h3>

- `YYYY-MM-DD` は **UTC 0 時**として扱われる
- `YYYY/MM/DD` は実装依存の**ローカル時刻**扱い
- Tokyo のローカル 0 時 = UTC だと**前日 15 時**

</div>
<div class="dark">

```js
// 「日付だけ」なら Date にしない
const date = Temporal.PlainDate.from("2026-01-01");
date.toString(); // "2026-01-01"

// 「瞬間」なら Instant
Temporal.Instant.from("2026-01-01T00:00:00Z");
```

</div>
</div>

<div class="callout">日付だけなのか、絶対時刻なのか。<strong>用途別に分ける</strong>と暗黙の変換が消える。</div>

---

<!-- _class: quiz -->

# Quiz 3. 存在しない日付を渡すと？
## 2026 年 2 月 30 日はありません。Date はどうする？

```js
console.log(new Date("2026-02-30").toISOString());
```

<div class="options">
<div class="option"><span class="letter">A</span><span>RangeError が投げられる</span></div>
<div class="option"><span class="letter">B</span><span>2026-03-02T00:00:00.000Z</span></div>
<div class="option"><span class="letter">C</span><span>Invalid Date</span></div>
</div>

---

# Answer 3. 正解は **B**。黙って丸めることがある
## 便利な補正は、本番データではバグの温床になる

<div class="ans-badge">B</div>

<div class="answer-body grid-2">
<div class="card">
<h3>Date で困ること</h3>

- 不正入力が**正常値のように**処理される
- 「ユーザーが 2/30 と入力した」**痕跡が消える**
- 検証と変換の境界が曖昧になる

</div>
<div class="dark">

```js
Temporal.PlainDate.from("2026-02-30");
// → RangeError: invalid range

Temporal.PlainTime.from("25:00");
// → RangeError
```

</div>
</div>

<div class="callout">Temporal は無理な値を<strong>暗黙に変換しない</strong>。失敗を失敗として扱える。</div>

---

# Temporal の基本思想
## Date を置き換える設計として、用途ごとにオブジェクトを分ける

<div class="grid-3x2">
<div class="card">
<h3>Instant</h3>
<div class="chip">UTC の瞬間</div>
<div class="desc">ログ、イベント順序、DB 保存</div>
</div>
<div class="card">
<h3>ZonedDateTime</h3>
<div class="chip">タイムゾーン込み</div>
<div class="desc">会議、店舗営業時間、DST</div>
</div>
<div class="card">
<h3>PlainDate</h3>
<div class="chip">日付だけ</div>
<div class="desc">請求日、休日、契約日</div>
</div>
<div class="card">
<h3>PlainTime</h3>
<div class="chip">時刻だけ</div>
<div class="desc">毎朝 8 時のアラーム</div>
</div>
<div class="card">
<h3>PlainYearMonth</h3>
<div class="chip">年月だけ</div>
<div class="desc">カード有効期限</div>
</div>
<div class="card">
<h3>Duration</h3>
<div class="chip">期間・差分</div>
<div class="desc">2 時間 30 分、1 ヶ月</div>
</div>
</div>

<div class="callout">Temporal は「日時 API」ではなく<strong>「日時の意味をオブジェクトで分ける API」</strong>。</div>

---

# Date の問題 → Temporal の対応
## クイズで見た問題は、用途別オブジェクトの設計で解消される

<div class="compare">

| Date の問題 | Temporal の対応 |
|---|---|
| setter がミュータブル | `add()` / `with()` は新しい値を返す |
| timestamp と年月日時分秒が混在 | `Instant` と `Plain*` / `ZonedDateTime` に分離 |
| UTC とローカル中心 | `ZonedDateTime` が `Asia/Tokyo` などのタイムゾーンを値として持つ |
| 日付だけ・時刻だけが苦手 | `PlainDate` / `PlainTime` が独立 |
| パースや不正値が紛れ込む | 各オブジェクトの `from()` で意図した形式として扱う |

</div>

---

# 使い始め方: まず「境界」を決める
## Node.js v26 でデフォルト有効。ブラウザは Safari 以外対応済み

<div class="grid-2" style="grid-template-columns: 1fr 1fr;">
<div class="card">
<h3>保存する</h3>
<div class="desc">イベント発生時刻は <code>Instant</code>。タイムゾーン表示は後で。</div>
</div>
<div class="card">
<h3>入力する</h3>
<div class="desc">フォームの日付は <code>PlainDate</code>、時刻は <code>PlainTime</code>。</div>
</div>
<div class="card">
<h3>予定を扱う</h3>
<div class="desc">地域のルール込みなら <code>ZonedDateTime</code>。夏時間 (DST) も含めて扱う。</div>
</div>
<div class="card">
<h3>計算する</h3>
<div class="desc"><code>{ days: 1 }</code> と <code>{ hours: 24 }</code> を別物として書く。</div>
</div>
</div>

<div class="callout">フロントは Safari 対応のため <strong>temporal-polyfill</strong>（20KB）で橋渡し。</div>

---

# まとめ
## Date を置き換える設計として、用途ごとにオブジェクトを使い分ける

<div class="sum-list">
<div class="sum-item"><span class="num">1</span><span>Date は <strong>1 つのオブジェクトに用途を詰め込みすぎ</strong>、使い分けが難しい設計になっている。</span></div>
<div class="sum-item"><span class="num">2</span><span>Temporal は <strong>用途別のオブジェクト (Instant / PlainDate / ZonedDateTime …)</strong> で、値の意味を明確にする。</span></div>
<div class="sum-item"><span class="num">3</span><span>日時を扱うときの問い:<br>「これは <strong>Instant</strong>？ <strong>PlainDate</strong>？ <strong>ZonedDateTime</strong>？」</span></div>
</div>

<div class="cta">次に Date を見たら、まず「何を表す値か」を確かめる。</div>

---

# 参考資料
## この資料は Qiita 記事を元に、公式情報で補足しています

<div class="ref">
<div class="ref-item"><b>Qiita:</b> Node.js v26 で標準化された JavaScript Temporal — Date の何が問題で、Temporal が何を解決するのか by @tamakiiii</div>
<div class="ref-item"><b>TC39:</b> Temporal proposal / Stage 4 Draft</div>
<div class="ref-item"><b>MDN:</b> Temporal - JavaScript / Date の課題と Temporal の概要</div>
<div class="ref-item"><b>Node.js:</b> Node.js v26.0.0 release notes - Temporal API enabled by default</div>
</div>
