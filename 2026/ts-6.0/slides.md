---
marp: true
theme: blueprint
paginate: true
size: 16:9
---

<!-- slide: 1 -->
<!-- _class: lead -->
# TypeScript 6.0 で
# 設定と移行はどう変わるか

---

<!-- slide: 2 -->
<!-- _class: lead -->
# TypeScript 6.0 RC is out

TypeScript 6.0 RC がリリースされた  
正式版の公開はもう近い

---

<!-- slide: 3 -->
<!-- _class: lead -->
# Are you ready for 6.0?

移行準備は整っているか

---

<!-- slide: 4 -->
<!-- _class: calm -->
# TS7 を見据えた移行準備が始まった

- 6.0 は現在の TypeScript 実装での最終メジャー予定
- 7.0 は Go 実装への移行が計画されている <span class="note-ref">[1]</span>
- 並列型チェックを見据えて挙動の決定性を整える

<p class="conclusion">今は「動く設定」だけでなく「TS7移行後も崩れにくい設定」を意識する</p>

<p class="note">[1] このGo化の対象は主にコンパイラ/言語サービスの実装であり、言語仕様そのものが変わる話ではない</p>

---

<!-- slide: 5 -->
<!-- _class: calm -->
# TS6 の軸は「暗黙依存と旧互換を減らす」

- `strict` / `types` などの暗黙既定を減らし、必要な設定を明示する
- `classic` 削除や `node10` 非推奨のように、旧互換ルートを減らす
- 解決規則を ESM 前提へ寄せ、環境差分を小さくする

<p class="conclusion">TS6 は、暗黙依存と旧互換を減らし、現在の標準前提へ寄せている</p>

---

<!-- slide: 6 -->
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

<p class="conclusion">TS6 では、型チェックの厳格化は追加施策ではなく標準前提になった</p>

---

<!-- slide: 7 -->
# `types` は自動読込から明示指定へ変わった

```json
{
  "types": []
}
```

- TS5: `types` 未指定なら `@types` を自動で拾う
- TS6: `types` のデフォルトが `[]` になり、自動読込しない

<p class="conclusion">どの型を読み込むかを明示し、環境ごとの揺れを減らす方向に変わった</p>

---

<!-- slide: 8 -->
<!-- _class: calm -->
# `types` は移行初手で固定する

- `types` 未指定では `process` や `describe` が解決できないケースが出る
- Node / Jest / Vitest など必要な型だけを明示指定する
- 必要な型を明示すると、環境差分を切り分けやすくなる

```text
暗黙のまま             先に固定する
types: 自動読み込み    types: ["node", "vitest"]
      ↓                      ↓
環境差分が出る         使う型を説明できる
```

<p class="conclusion"><code>types</code> は「必要な型を使う設定」として最初に固定する</p>

---

<!-- slide: 9 -->
<!-- _class: calm -->
# `rootDir` も移行初手で固定する

- TS5: `rootDir` 未指定なら、入力ファイル群の共通親ディレクトリから推論される
- TS6: `tsconfig.json` があると、`rootDir` 未指定の既定は `tsconfig.json` のあるディレクトリになる
- コンパイルは通っても、出力構造だけ崩れることがある
- 先に固定しておくと、後続の差分を切り分けやすい

```text
src/index.ts, outDir: dist のとき
TS5: rootDir = src   → dist/index.js
TS6: rootDir = tsconfig の場所 → dist/src/index.js
```

<p class="conclusion"><code>rootDir</code> は「出力構造の基準になる設定」として先に決める</p>

---

<!-- slide: 10 -->
# `target` と `module` の既定は現在主流の実行環境に寄った

- 現在主流の実行環境に合わせてデフォルトが見直された
- `target` のデフォルトは `es2025` になる
- `module` のデフォルトは `esnext` になる
- ES5 向け互換が必要な場合は、別途ビルド工程で対応する
  - 例: Babel / SWC / esbuild で ES5 向けに変換する
  - 例: 互換向け polyfill を配布側で注入する

<p class="conclusion">古い環境互換は、TypeScript設定ではなくビルド工程で分離管理する</p>

---

<!-- slide: 11 -->
# `moduleResolution` は Node か Bundler かで先に決める

- `classic` は削除
- `node` (`node10`) は非推奨
- 実行環境に応じて `nodenext` / `bundler` を選ぶ

<p class="conclusion">Node 直実行か Bundler 中心かを先に決める</p>

---

<!-- slide: 12 -->
# `baseUrl` は非推奨になり、import 解決は `paths` 明示へ寄せる

```json
{
  "baseUrl": "./"
}
```

- `baseUrl` は非推奨になった
- import 解決は `paths` で明示する方向に整理された
- 旧挙動が必要な場合は `paths` に `*` マッピングを追加する

<p class="conclusion">import 解決の起点は暗黙に置かず、<code>paths</code> で明示する</p>

---

<!-- slide: 13 -->
# `import assertions` は `with` へ移行する

```ts
// before
import data from "./a.json" asserts { type: "json" }

// after
import data from "./a.json" with { type: "json" }
```

- `tsconfig` の話ではないが、移行時に押さえるべき標準構文側の変更
- JSON import などでは、構文の書き換えが必要になる
<p class="conclusion">JavaScript標準化の流れに合わせて、import の構文は asserts から with へ移行した</p>

---

<!-- slide: 14 -->
# `dom.iterable` / `dom.asynciterable` は足さなくてよくなった

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

<p class="conclusion"><code>lib</code> 設定も「足す前提」から「最小指定」へ寄っている</p>

---

<!-- slide: 15 -->
# 副作用 import の解決ミスは既定で見つかりやすくなる

`noUncheckedSideEffectImports: true` が既定になった

```ts
// 副作用 import
import "./setup";
```

- 副作用 import 自体は引き続き使える
- ただし、解決できない副作用 import は TS6 では見逃されにくくなった
- CSS import やパスエイリアスで問題が出る場合は、解決設定や宣言ファイルを見直す

<p class="conclusion">TS6 は「見逃されていた副作用 import の解決ミス」を見つけやすくする</p>

---

<!-- slide: 16 -->
# `stableTypeOrdering` は比較時だけ一時的に使う

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

<!-- slide: 17 -->
# 問題は「同じ意味でも表示順が揺れる」こと

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

- 余計な定義が 1 つ増えるだけで `.d.ts` の union 順序が変わることがある

<p class="conclusion">差分比較では「意味の差」ではなく「順序の差」がノイズになる</p>

---

<!-- slide: 18 -->
# `stableTypeOrdering` を使うと比較ノイズを減らせる

| モード | `foo` 戻り値型（`.d.ts`） | 備考 |
|---|---|---|
| TS6 (flagなし) | `100 \| 500` / `500 \| 100` | 生成順で揺れる |
| TS6 (+flag) | TS7 と同じ順序 | 比較ノイズ減 |
| TS7 | 安定順序 | 同じ入力で同じ順序 |

<p class="conclusion">TS6/TS7 比較では、まず順序ノイズを消してから差分を見る</p>

---

<!-- slide: 19 -->
# `stableTypeOrdering` は常用ではなく移行用

- 常時ONではなく、移行検証で一時的に有効化する
- 型チェックが最大 25% 程度遅くなる可能性がある
- TS6/TS7 比較で本質的な差分を見つけやすくする
- 推論差で崩れる場合は型引数・変数注釈を明示する

<p class="conclusion">常用ではなく、移行時の差分診断で使う</p>

---

<!-- slide: 20 -->
# 先に確認すべき変更と、後から見ればよい改善を分ける

- まず確認すべきなのは、移行に影響する変更と非推奨項目
- 細かな改善は、移行対応とは分けて確認すると整理しやすい
- 例:
  - `es2025` では `RegExp.escape` などの型が使える
  - `esnext` では `Temporal` など次期標準 API の型が使える

<p class="conclusion">まずは移行に影響する変更を押さえ、その後に細かな改善を見る</p>

---

<!-- slide: 21 -->
<!-- _class: calm -->
# 移行時はこの順で見ると切り分けしやすい

1. `types` / `rootDir` を明示して固定
2. `moduleResolution` と `module` を実行環境に合わせる
3. 見つかった import 解決エラーと非推奨設定を潰す
   - `baseUrl` は `paths` 明示へ移行する
   - `noUncheckedSideEffectImports` で見つかった副作用 import の解決ミスを直す
   - `moduleResolution: node` は `nodenext` / `bundler` へ移行する
   - `target: es5` は互換ビルド工程へ分離する
4. `import ... with` へ構文移行

<p class="conclusion"><code>tsc --noEmit</code> で破壊的変更を確認し、必要に応じて <code>.d.ts</code> / エラーメッセージ差分も見る</p>

---

<!-- slide: 22 -->
# TS6 は前提を現在主流の開発実態に合わせて揃え直す

- 暗黙依存を減らし、必要な設定を明示する
- ESM と現在主流の実行環境を標準前提にする
- TS7 への移行を見据えた設定へ寄せる

<p class="conclusion">TS6 は「新機能を足す」より「前提を現在主流の開発実態に合わせて揃え直す」リリースである</p>

---

<!-- slide: 23 -->
# 参考資料

- [TypeScript 6.0 Beta Announcement](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/)
- [TypeScript 6.0 RC Announcement](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/)

---

<!-- slide: 24 -->
<!-- _class: lead -->
# Thank You
