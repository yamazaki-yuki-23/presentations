---
marp: true
theme: gaia
paginate: true
size: 16:9
---

<!-- slide: 1 -->
# TypeScript 6.0

## 機能追加より「前提の更新」を読む

---

<!-- slide: 2 -->
# 今日のゴールは差分暗記ではない

- 変更点を網羅する会ではない
- 「何が標準前提になったか」を掴む
- 明日からの `tsconfig` 判断を速くする

**持ち帰り: 6.0 は移行判断の基準を更新するリリース**

---

<!-- slide: 3 -->
# TS6 は TS7 への橋渡しである

- 6.0 は現行実装系での最終メジャー予定
- 7.0 は Go 実装への移行が計画されている
- 並列型チェックを見据えて挙動の決定性を整える

**今は「動く設定」より「次でも崩れない設定」を選ぶ**

---

<!-- slide: 4 -->
# 本質は「暗黙を減らし、明示を増やす」こと

- 自動で拾う挙動を減らす
- レガシー互換の枝分かれを減らす
- ESM 前提の解決規則に寄せる

**設計思想は一貫している: 予測可能性の強化**

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
# まず壊れやすいのは `types` と `rootDir`

- `types` 未明示で `process` や `describe` が解決不能
- `rootDir` 未明示で出力先が `dist/src/...` にズレる
- ここは最初に固定すると移行事故が減る

**移行初手は機能追加ではなく設定の固定**

---

<!-- slide: 8 -->
# `target` と `module` はモダン実行環境が基準

- `target` は最新 ECMAScript 年度へ寄る
- `module` は `esnext` が既定
- ES5 前提の運用は標準コースから外れる

**古い環境互換は別レイヤーで管理する**

---

<!-- slide: 9 -->
# `moduleResolution` は ESM 実態に寄せる

- `classic` は削除
- `node` (`node10`) は非推奨
- `nodenext` / `bundler` を選ぶ時代

**Node 直実行か Bundler 中心かを先に決める**

---

<!-- slide: 10 -->
# `baseUrl` 単体運用は非推奨になった

```json
{
  "baseUrl": "./"
}
```

- 単体では解決規則が曖昧になりやすい
- ツールごとの差異を招きやすい
- 必要なら `paths` まで明示して管理する

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

**TS 独自より JavaScript 標準への整合を優先**

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

**先に土台設定、その後に機能活用**

---

<!-- slide: 15 -->
# 移行優先順位はこの順で進める

1. `types` / `rootDir` を明示して固定
2. `moduleResolution` と `module` を現実に合わせる
3. 非推奨 (`baseUrl` 単体, `node`, `es5`) を整理
4. `import ... with` へ構文移行

**CI で `tsc --noEmit` を回し、差分を可視化する**

---

<!-- slide: 16 -->
# まとめ: TS6 は「構造改革」である

- 暗黙依存を減らし、明示設定を増やす
- ESM とモダンランタイムを標準前提にする
- TS7 移行で困らない設計へ寄せる

**判断軸は「今通るか」より「次でも維持できるか」**

---

<!-- slide: 17 -->
# Q & A
