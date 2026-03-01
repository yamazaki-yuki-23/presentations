---
marp: true
theme: gaia
paginate: true
size: 16:9
---

# TypeScript 6.0
## 何を整理し、何を変えたのか

---

# 今日の視点

> 変更点の網羅ではない  
> **思想の転換を読む**

---

# TypeScript 6.0 の位置づけ

- JS実装最後のメジャー
- TS7はGo実装
- 並列型チェックを前提に再設計

---

# TS6 の本質

## 暗黙を削る
## 古い互換を切る
## ESM前提へ移行する

---

# strict は前提になった

```json
{
  "strict": true
}
```

型安全は「選択肢」ではない。

---

# types は空になる

```json
{
  "types": []
}
```

- @types 自動収集しない
- グローバル環境は明示せよ
- パフォーマンス改善

---

# target / module の再定義

- target → 最新年度
- module → esnext

古いランタイムは標準ではない。

---

# baseUrl は非推奨

```json
{
  "baseUrl": "./"
}
```

曖昧な解決を排除する。

paths を明示せよ。

---

# moduleResolution の転換

- classic → 削除
- node → 非推奨
- nodenext / bundler へ

ESM解決アルゴリズムに準拠する。

---

# import asserts は終わった

```ts
import data from "./a.json" asserts { type: "json" }
```

↓

```ts
import data from "./a.json" with { type: "json" }
```

TS独自仕様から標準へ。

---

# dom.iterable の統合

```json
{
  "lib": ["dom"]
}
```

互換レイヤーの整理。

---

# stableTypeOrdering

```json
{
  "stableTypeOrdering": true
}
```

TS7 の並列型チェックに備える。

---

# 小さな改善

- this 推論改善
- es2025 lib
- RegExp.escape
- Temporal
- Map upsert

---

# 結論

TypeScript 6.0 は

## 構造改革である

---

# 我々が意識すべきこと

- 明示する
- strict 前提で設計する
- ESM前提で考える
- 7.0を見据える

---

# Q & A
