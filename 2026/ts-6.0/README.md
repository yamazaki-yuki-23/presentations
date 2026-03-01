# TypeScript 6.0 - 何が変わり、なぜ重要か

この発表では、TypeScript 6.0 で導入された構造的な変更を扱います。

細かな更新を網羅するのではなく、次の観点に絞って説明します。

- 暗黙的な挙動の削減
- ESMファースト設計への移行
- 実プロジェクトに影響する破壊的変更
- TypeScript 7.0（ネイティブ実装）への準備

---

## 概要

TypeScript 6.0 は一見すると段階的なアップデートに見えます。

一方で、TypeScript エコシステム全体では構造転換が進んでいます。

- デフォルト設定はより厳格な方向へ移行
- 暗黙的なグローバル挙動の削除
- レガシー互換レイヤーの縮小
- 並列型チェックを見据えたコンパイラ設計への準備

---

## 主なトピック

### 1. デフォルト設定と明示性

- `strict` のデフォルトが `true`
- `types` のデフォルトが `[]`
- `target` / `module` のデフォルト変更

### 2. モジュールシステムの再設計

- `baseUrl` の非推奨化
- `moduleResolution` の再設計
- `nodenext` / `bundler` への移行

### 3. 破壊的変更

- `import ... asserts` から `with`（import attributes）へ
- `target: es5` の非推奨化
- `classic` 解決方式の削除
- `dom.iterable` の統合

### 4. TypeScript 7.0 への準備

- `stableTypeOrdering`
- コンパイラの決定性（determinism）
- 並列型チェックへの影響

---

## 重要なポイント

TypeScript 6.0 は単なる機能追加ではありません。

次のような構造的整理が進んでいます。

- 曖昧さの削減
- 設定の明示化の促進
- モダンな ECMAScript 標準との整合
- 大規模なコンパイラ移行への準備

---

## スライド

このディレクトリの `slides.md` を参照してください。

---

## 参考資料

- 公式アナウンス:  
  https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/

- TypeScript 6.0 関連の議論・ドキュメント
