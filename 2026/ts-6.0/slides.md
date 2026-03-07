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

<p class="conclusion">今は「動く設定」より「TS7時代でも崩れない設定」を選ぶ</p>

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
# `strict` は推奨から標準前提へ変わった

```json
{
  "strict": true
}
```

- 新規プロジェクトの初期値が変わる
- 「後で厳しくする」戦略は負債化しやすい
- 緩い設定は例外として明示管理する

---

<!-- slide: 6 -->
# `types: []` は壊すためでなく混入を止めるため

```json
{
  "types": []
}
```

- `@types` の自動流入を止める
- Node / Jest / Vitest を必要分だけ列挙する
- 型解決の速度と再現性が上がる

---

<!-- slide: 7 -->
<!-- _class: calm -->
# まず壊れやすいのは `types` と `rootDir`

- `types` 未明示で `process` や `describe` が解決不能
- `rootDir` 未明示で出力先が `dist/src/...` にズレる
- ここは最初に固定すると移行事故が減る

<p class="conclusion">移行初手は機能追加ではなく設定の固定</p>

---

<!-- slide: 8 -->
# `target` と `module` はモダン実行環境が基準

- `target` は最新 ECMAScript 年度へ寄る
- `module` は `esnext` が既定
- ES5 前提の運用は標準コースから外れる

<p class="conclusion">古い環境互換は別レイヤーで管理する</p>

---

<!-- slide: 9 -->
# `moduleResolution` は ESM 実態に寄せる

- `classic` は削除
- `node` (`node10`) は非推奨
- `nodenext` / `bundler` を選ぶ時代

<p class="conclusion">Node 直実行か Bundler 中心かを先に決める</p>

---

<!-- slide: 10 -->
# `--baseUrl` は deprecated になった

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
# `import asserts` は `with` へ移行する

```ts
import data from "./a.json" asserts { type: "json" }
```

移行後

```ts
import data from "./a.json" with { type: "json" }
```

<p class="conclusion">TS 独自より JavaScript 標準への整合を優先</p>

---

<!-- slide: 12 -->
# `dom.iterable` 統合は小さいが方向性は大きい

```json
{
  "lib": ["dom"]
}
```

- 互換目的の細かな指定が不要になる
- `lib` 設定の分岐が減る
- レガシー整理の流れを示す変更

---

<!-- slide: 13 -->
# `stableTypeOrdering` は TS7 比較の実務フラグ

```json
{
  "stableTypeOrdering": true
}
```

- 並列化しても型順序のノイズ差分を減らす
- 6.x と 7.x の差分検証をしやすくする
- 常時 ON ではなく移行検証で使う

---

<!-- slide: 14 -->
# 細かな改善は「後回し」でよい

- `this` 推論改善
- `es2025` lib
- `RegExp.escape`
- `Temporal`
- `Map` / `WeakMap` upsert 系

<p class="conclusion">先に土台設定、その後に機能活用</p>

---

<!-- slide: 15 -->
<!-- _class: calm -->
# 移行優先順位はこの順で進める

1. `types` / `rootDir` を明示して固定
2. `moduleResolution` と `module` を現実に合わせる
3. 非推奨 (`baseUrl`, `node`, `es5`) を整理
4. `import ... with` へ構文移行

<p class="conclusion">CI で `tsc --noEmit` を回し、差分を可視化する</p>

---

<!-- slide: 16 -->
# まとめ: TS6 は「構造改革」である

- 暗黙依存を減らし、明示設定を増やす
- ESM とモダンランタイムを標準前提にする
- TS7 移行で困らない設計へ寄せる

<p class="conclusion">判断軸は「今通るか」より「次でも維持できるか」</p>

---

<!-- slide: 17 -->
# Q & A
