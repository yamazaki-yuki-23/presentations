# TypeScript 6.0 – Speaker Notes

---

## Slide 1 – タイトル

今日は TypeScript 6.0 の変更点を扱います。

ただし、変更点を網羅することが目的ではありません。

今回のテーマは：

> TypeScriptが「何を捨て、何を前提にしたのか」

です。

6.0は地味に見えますが、実は構造改革です。

---

## Slide 2 – 今日の視点

今日は機能の紹介ではなく、思想の転換を読みます。

TypeScriptはこれまで「互換性重視」でした。

6.0ではその前提を整理し始めています。

---

## Slide 3 – 位置づけ

6.0はJavaScript実装ベースでの最後のメジャー予定です。

7.0ではGo実装への移行が予定されています。

つまり、6.0は橋渡し。

並列型チェックを見据えた設計変更が含まれています。

---

## Slide 4 – strict default true

strictがデフォルトになりました。

これは単なる設定変更ではありません。

型安全は「選択肢」ではなく「前提」になったということです。

TypeScriptエコシステムが成熟した証拠です。

---

## Slide 5 – types default []

ここが実務的に一まわ壊れやすい変更です。

これまでは node_modules/@types が自動で読み込まれていました。

6.0ではそれがなくなります。

理由は：

- グローバル汚染の回避
- パフォーマンス改善
- 明示主義への移行

今後は types を明示することが前提になります。

---

## Slide 6 – target / module

targetは最新年度へ。

moduleはesnextへ。

ES5は標準前提ではなくなりました。

これは「現代JavaScriptを前提にする」という宣言です。

---

## Slide 7 – baseUrl 非推奨

baseUrlはこれまでlookup rootとして使われていました。

しかしこれはモジュール解決の曖昧さを生みます。

pathsはprefix mappingであるべきです。

TypeScriptは解決を決定的にしようとしています。

---

## Slide 8 – moduleResolution 再定義

classicは削除。

nodeはnode10相当で非推奨。

nodenextやbundlerへ。

これはESM解決アルゴリズムへの完全移行です。

CommonJS中心設計からの脱却です。

---

## Slide 9 – import asserts → with

asserts構文は非推奨になります。

代わりにwithを使います。

これはECMAScriptのimport attributes proposalに追従したものです。

TypeScript独自仕様を減らしています。

---

## Slide 10 – target es5 非推奨

ダウンレベル変換はTypeScriptの主戦場ではなくなりました。

バンドラやトランスパイラへ責務を移しています。

古い互換レイヤーの整理です。

---

## Slide 11 – dom.iterable 統合

lib設定の整理です。

dom.iterableはdomに統合されました。

小さい変更ですが、

「互換レイヤーを減らす」という思想の象徴です。

---

## Slide 12 – stableTypeOrdering

これは7.0への布石です。

型IDはこれまで encounter order に依存していました。

並列型チェックでは順序が不安定になります。

そのため、順序を決定的にする必要があります。

これはコンパイラ内部設計の変化を示しています。

---

## Slide 13 – this推論改善

contextually sensitive function判定の調整です。

DX改善です。

思想的インパクトは小さいですが、品質向上です。

---

## Slide 14 – まとめ

TypeScript 6.0 は：

- 暗黙を削る
- 互換を整理する
- ESM前提へ移行する
- 並列型チェックへ備える

6.0は地味ではありません。

構造改革です。

今後は「明示」を前提に設計する必要があります。

---

# 参考資料

## 公式発表

- TypeScript 6.0 Beta Announcement  
  https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-beta/

## 補足

- 本発表は公式アナウンス記事を一次情報として整理しています。
- 変更点の網羅ではなく、設計思想と実務影響に焦点を当てています。
- TypeScript 7.0（Go実装）への移行を見据えた変更という観点で解釈しています。
