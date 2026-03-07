---
marp: true
theme: blueprint
paginate: true
size: 16:9
---

<!-- slide: 1 -->
<!-- _class: lead -->
# TypeScript 6.0

## 機能追加より「設計意図」を読む

---

<!-- slide: 2 -->
<!-- _class: calm -->
# 今日のゴール: 何をどう見るか

- 変更点を網羅する会ではない
- 個別機能より、`tsconfig` 変更の設計意図を見る
- TS6 が何を捨て、何を標準にしたかを掴む

<p class="conclusion">6.0 は機能追加より設計方針の転換を読むリリース</p>

---

<!-- slide: 3 -->
<!-- _class: calm -->
# TS6 は TS7 への橋渡しである

- 6.0 は現行実装系での最終メジャー予定
- 7.0 は Go 実装への移行が計画されている <span class="note-ref">[1]</span>
- 並列型チェックを見据えて挙動の決定性を整える

<p class="conclusion">今は「動く設定」より「TS7移行後でも崩れない設定」を選ぶ</p>

<p class="note">[1] このGo化の対象は主にコンパイラ/言語サービスの実装であり、言語仕様そのものが変わる話ではない</p>

---

<!-- slide: 4 -->
<!-- _class: calm -->
# TS6 の設計の軸は「暗黙を減らし、明示を増やす」

- `strict` / `types` などの暗黙既定を減らし、必要な設定を明示する
- `classic` 削除や `node10` 非推奨のように、旧互換ルートを減らす
- 解決規則を ESM 前提へ寄せ、環境差分を小さくする

<p class="conclusion">TS6は、暗黙依存を減らして「設定で挙動を揃える」方向に寄せている</p>

---

<!-- slide: 5 -->
# `strict` は推奨からデフォルトへ変わった

```json
{
  "strict": true
}
```

- 新規プロジェクトの初期値が変わる
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
  - Node / Jest / Vitest など必要な型だけを明示指定する
  - 不要な型読込を減らし、型解決のブレを抑える

---

<!-- slide: 7 -->
<!-- _class: calm -->
# 初手で固定したい設定は `types` と `rootDir`

- `types` を指定しないと `process` や `describe` が解決できないケースが出る
- `rootDir` を指定しないと出力先が `dist/src/...` にズレる場合がある <span class="note-ref">[1]</span>
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

<p class="conclusion">JavaScript標準化の流れに合わせて、import の構文は asserts から with へ移行した</p>

---

<!-- slide: 12 -->
# `dom` に `dom.iterable` / `dom.asynciterable` が統合された

```json
{
  // before
  "lib": ["dom", "dom.iterable"]
  // after
  "lib": ["dom"]
}
```

- TS6 では `lib.dom.iterable.d.ts` / `lib.dom.asynciterable.d.ts` が `lib.dom.d.ts` に含まれる
- `dom.iterable` / `dom.asynciterable` 指定は可能だが実体は空ファイル

---

<!-- slide: 13 -->
# `stableTypeOrdering` は TS6/TS7 比較用オプション

```json
// tsconfig.json
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
# 細かな改善は後段で対応する

- this なし関数の型推論改善
- `lib` に `es2025` を指定すると、ES2025 API の型が使える
  - `RegExp.escape`（文字列を正規表現用に安全にエスケープ）
- `lib` に `esnext` を指定すると、次期標準APIの型が使える
  - `Temporal`（次世代日時APIの型定義）
  - `Map` / `WeakMap` upsert 系（存在時は更新、未存在時は追加）

いずれも有用だが、移行初期の成否を左右する項目ではない

<p class="conclusion">先に tsconfig の移行項目を確定し、その後に新機能を取り込む</p>

---

<!-- slide: 19 -->
<!-- _class: calm -->
# 移行優先順位はこの順で進める

1. `types` / `rootDir` を明示して固定
2. `moduleResolution` と `module` を実行環境に合わせる
3. 非推奨の設定を置換先へ移行する
   - `baseUrl` は `paths` 明示へ移行する
   - `moduleResolution: node` は `nodenext` / `bundler` へ移行する
   - `target: es5` は互換ビルド工程へ分離する
4. `import ... with` へ構文移行

<p class="conclusion"><code>tsc --noEmit</code> で破壊的変更を検知し、必要時に <code>.d.ts</code> / エラーメッセージ差分を比較する</p>

---

<!-- slide: 20 -->
# まとめ: TS6 は「設定方針の転換」である

- 暗黙依存を減らし、明示設定を増やす
- ESM と現在主流の実行環境を標準前提にする
- TS7 への移行を見据えた設定へ寄せる

<p class="conclusion">判断軸は「今通るか」より「次でも維持できるか」</p>

---

<!-- slide: 21 -->
<!-- _class: lead -->
# Thank You
