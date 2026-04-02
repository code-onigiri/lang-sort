# lang-sort
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

日本語 | [English](README_en.md)

`lang-sort` は、Minecraftの多言語対応のための言語ファイル（`lang/xx_xx.json` / `lang/xx_xx.lang`）を賢くソートするCLIツールです。

キーの形式を利用してソートするため、クエストの言語ファイルには効果的ではありません。 
別途、FTBQuest用のソートツール[ftbq-sort](https://github.com/he1se1/ftbq-sort)を公開しています。

Minecraft v1.12.2-1.20のlangファイルに対応しています。

* v1.12.2: `.lang` 形式
* v1.13+: `.json` 形式

## 🚀 インストール (Installation)

Python 3.8以上が必要です。環境を汚さない `uv` または `pipx` を使用したインストールを推奨します。

```bash
uv tool install git+https://github.com/he1se1/lang-sort.git
```

```bash
pipx install git+https://github.com/he1se1/lang-sort.git
```

## 🛠 使い方 (Usage)

インストールすると、グローバルに `lang-sort` コマンドが使用できるようになります。

```bash
lang-sort <入力langファイルのパス> <出力langファイルのパス>
```

### 引数の説明

* `lang_in`: ソートしたい元の言語ファイル（`.json` / `.lang`）のパスを指定します。
* `lang_out`: 整列済みのデータを出力する先のファイルパスを指定します。（入力ファイルと同じパスを指定して上書きすることも可能です）

拡張子から形式を自動判定します（`.json` / `.lang`）。必要に応じて `--input-format` / `--output-format` で明示指定できます。

### 実行例

```bash
lang-sort ./kubejs/assets/kubejs/lang/ja_jp.json ./kubejs/assets/kubejs/lang/ja_jp_sorted.json
```
(あとで `ja_jp_sorted.json` を `ja_jp.json` にリネームして上書きしないとゲームに反映されないことに注意してください)

```bash
lang-sort ./assets/examplemod/lang/ja_jp.lang ./assets/examplemod/lang/ja_jp_sorted.lang
```

## 📝 依存ライブラリ
ありません。
