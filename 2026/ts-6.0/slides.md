---
marp: true
theme: blueprint
paginate: true
size: 16:9
---

<!-- slide: 1 -->
<!-- _class: lead -->
# TypeScript 6.0 設定と移行の考え方はどう変わったか

---

<!-- slide: 2 -->
<!-- _class: calm -->
# 今日のゴール: 設定と移行の考え方の変化を掴む

- 変更点の網羅は目的にしない
- 個別機能より、設定の前提がどう変わったかを見る
- TS6 が何を標準にし、何を明示する方向へ寄せたかを掴む

<p class="conclusion">TS6 では、何が増えたか以上に「どう設定し、どう移行するか」が重要になる</p>

---

<!-- slide: 3 -->
<!-- _class: calm -->
# TS6 は TS7 への橋渡しである

- 6.0 は現行実装系での最終メジャー予定
- 7.0 は Go 実装への移行が計画されている <span class="note-ref">[1]</span>
- 並列型チェックを見据えて挙動の決定性を整える

<p class="conclusion">今は「動く設定」だけでなく「TS7移行後も崩れにくい設定」を意識する</p>

<p class="note">[1] このGo化の対象は主にコンパイラ/言語サービスの実装であり、言語仕様そのものが変わる話ではない</p>

---

<!-- slide: 4 -->
<!-- _class: calm -->
# TS6 の軸は「暗黙依存と旧互換を減らす」

- `strict` / `types` などの暗黙既定を減らし、必要な設定を明示する
- `classic` 削除や `node10` 非推奨のように、旧互換ルートを減らす
- 解決規則を ESM 前提へ寄せ、環境差分を小さくする

<p class="conclusion">TS6 は、暗黙依存と旧互換を減らし、現在の標準前提へ寄せている</p>

---

<!-- slide: 5 -->
# `strict` は推奨からデフォルトへ変わった

```json
{
  "strict": true
}
```

- 新規プロジェクトの初期値が変わる
- 新規開発で `strict` 前提が一般化しており、既定値もその実態に寄った
- 「後で厳しくする」戦略は負債化しやすい
- 緩い運用にするなら、`strict: false` を明示して使う

---

<!-- slide: 6 -->
# `types` のデフォルト変更で型の読込方針が変わる

```json
{
  "types": []
}
```

- TS5: `types` 未指定なら `@types` を自動で拾う
- TS6: `types` のデフォルトが `[]` になり、自動読込しない
- 型は自動流入に任せず、必要なものを明示指定する方向に変わった
  - Node / Jest / Vitest など必要な型だけを明示指定する
  - 不要な型読込を減らし、型解決のブレを抑える

---

<!-- slide: 7 -->
<!-- _class: calm -->
# 初手で固定したい設定は `types` と `rootDir`

- `types` を指定しないと `process` や `describe` が解決できないケースが出る
- `rootDir` を指定しないと出力先が `dist/src/...` にズレる場合がある <span class="note-ref">[1]</span>
- 移行時は後回しにせず、先に明示して設定の揺れを止める
- ここを先に固定すると移行時の事故を減らせる

<p class="conclusion">移行初手は機能追加ではなく設定の固定</p>

<p class="note">[1] `dist/src/...` は典型例。出力先はプロジェクト構成や他の設定によって変わる</p>

---

<!-- slide: 8 -->
# `target` と `module` のデフォルトが見直された

- 現在主流の実行環境（evergreen）に合わせてデフォルトが見直された
- `target` のデフォルトは `es2025` になる
- `module` のデフォルトは `esnext` になる
- ES5 向け互換が必要な場合は、別途ビルド工程で対応する
  - 例: Babel / SWC / esbuild で ES5 向けに変換する
  - 例: 互換向け polyfill を配布側で注入する

<p class="conclusion">古い環境互換は、TypeScript設定ではなくビルド工程で分離管理する</p>

---

<!-- slide: 9 -->
# `moduleResolution` は実行環境に合わせて選ぶ

- `classic` は削除
- `node` (`node10`) は非推奨
- 実行環境に応じて `nodenext` / `bundler` を選ぶ

<p class="conclusion">Node 直実行か Bundler 中心かを先に決める</p>

---

<!-- slide: 10 -->
# `baseUrl` は deprecated になった

```json
{
  "baseUrl": "./"
}
```

- `baseUrl` を import 解決の基準ディレクトリとして使う挙動が廃止される
- 暗黙の探索起点を減らし、解決規則を `paths` で明示する方向に整理された
- `paths` で使う共通接頭辞は各エントリに明示する
- 旧挙動が必要な場合は `paths` に `*` マッピングを追加する

---

<!-- slide: 11 -->
# `import assertions` は `with` へ置き換わる

```ts
// before
import data from "./a.json" asserts { type: "json" }

// after
import data from "./a.json" with { type: "json" }
```

- 設定変更ではないが、移行時に押さえるべき標準構文側の変更
<p class="conclusion">JavaScript標準化の流れに合わせて、import の構文は asserts から with へ移行した</p>

---

<!-- slide: 12 -->
# `dom.iterable` / `dom.asynciterable` は `dom` に統合された

```json
{
  // before
  "lib": ["dom", "dom.iterable"]
  // after
  "lib": ["dom"]
}
```

- TS6 では両方の定義が `lib.dom.d.ts` に含まれる
- `lib` 指定も、冗長な組み合わせを前提にしない方向で整理された
- 指定自体は可能だが、実体は空ファイル

---

<!-- slide: 13 -->
# `stableTypeOrdering` は TS6/TS7 比較用オプション

```json
{
  "compilerOptions": {
    "stableTypeOrdering": true
  }
}
```

- TS6 と TS7 の出力・診断差分を比較するときに使う
- TS6 の型順序挙動を TS7 に寄せ、差分ノイズを減らす

<p class="conclusion">移行時の比較ノイズを減らすために使う</p>

---

<!-- slide: 14 -->
# TS6 / TS6+flag / TS7 の結果比較

```ts
// base.ts
export function foo(condition: boolean) {
  return condition ? 100 : 500;
}

// with-extra.ts
const x = 500;
export function foo(condition: boolean) {
  return condition ? 100 : 500;
}
```

- この入力で `.d.ts` の union 順序がどう出るかを比較する

---

<!-- slide: 15 -->
## 同じ入力での出力比較
| モード | `foo` 戻り値型（`.d.ts`） | 備考 |
|---|---|---|
| TS6 (flagなし) | `100 \| 500` / `500 \| 100` | 生成順で揺れる |
| TS6 (+flag) | TS7 と同じ順序 | 比較ノイズ減 |
| TS7 | 安定順序 | 同じ入力で同じ順序 |

---

<!-- slide: 16 -->
# TS7 で順序が安定化される理由

- TS6 までは型生成順（内部ID順）が表示順に影響しやすい
- TS7 では型構造ベースの決定的な並び順へ移行する
- Go 実装・並列型チェックでも順序を安定させる狙いがある

<p class="conclusion">安定順序は「同じ入力なら同じ出力」に寄せるための変更</p>

---

<!-- slide: 17 -->
# `stableTypeOrdering` の使いどころ

- 常時ONではなく、移行検証で一時的に有効化する
- 型チェックが最大 25% 程度遅くなる可能性がある
- TS6/TS7 比較で本質的な差分を見つけやすくする
- 推論差で崩れる場合は型引数・変数注釈を明示する

<p class="conclusion">常用ではなく、移行時の差分診断で使う</p>

---

<!-- slide: 18 -->
# 細かな改善は移行項目と分けて見る

- this なし関数の型推論改善
- `lib` に `es2025` を指定すると、ES2025 API の型が使える
  - `RegExp.escape`（文字列を正規表現用に安全にエスケープ）
- `lib` に `esnext` を指定すると、次期標準APIの型が使える
  - `Temporal`（次世代日時APIの型定義）
  - `Map` / `WeakMap` upsert 系（存在時は更新、未存在時は追加）
- いずれも有用だが、まず押さえたい移行項目とは分けて見る

<p class="conclusion">まずは移行に関わる設定変更を押さえ、その後に個別改善を見る</p>

---

<!-- slide: 19 -->
<!-- _class: calm -->
# 移行時はこの順で見ると整理しやすい

1. `types` / `rootDir` を明示して固定
2. `moduleResolution` と `module` を実行環境に合わせる
3. 非推奨の設定を置換先へ移行する
   - `baseUrl` は `paths` 明示へ移行する
   - `moduleResolution: node` は `nodenext` / `bundler` へ移行する
   - `target: es5` は互換ビルド工程へ分離する
4. `import ... with` へ構文移行

<p class="conclusion"><code>tsc --noEmit</code> で破壊的変更を確認し、必要に応じて <code>.d.ts</code> / エラーメッセージ差分も見る</p>

---

<!-- slide: 20 -->
# まとめ: TS6 は設定と移行の考え方を変えるリリース

- 暗黙依存を減らし、明示設定を増やす
- ESM と現在主流の実行環境を標準前提にする
- TS7 への移行を見据えた設定へ寄せる

---

<!-- slide: 21 -->
<!-- _class: lead -->
# Thank You
