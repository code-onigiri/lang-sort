# lang-sort
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

[日本語](README.md) | English

`lang-sort` is a CLI tool designed to smartly sort Minecraft localization files (`lang/xx_xx.json` / `lang/xx_xx.lang`).

Because it utilizes key formats for sorting, it is not effective for quest language files. 
I have published a specifical sorting tool for FTB Quests: [ftbq-sort](https://github.com/he1se1/ftbq-sort).

Supports lang files for Minecraft v1.12.2-1.20.

* v1.12.2: `.lang` format
* v1.13+: `.json` format

## 🚀 Installation

Python 3.8 or higher is required. We recommend installing using `uv` or `pipx` to keep your environment clean.

```bash
uv tool install git+https://github.com/he1se1/lang-sort.git
```

```bash
pipx install git+https://github.com/he1se1/lang-sort.git
```

## 🛠 Usage

Once installed, the `lang-sort` command will be available globally.

```bash
lang-sort <input_lang_file_path> <output_lang_file_path>
```

### Arguments

* `input_lang_file_path`: The path to the original language file (`.json` / `.lang`) you want to sort.
* `output_lang_file_path`: The path where the sorted data will be output. (You can specify the same path as the input file to overwrite it directly).

The tool auto-detects format from extension (`.json` / `.lang`). You can override it with `--input-format` and `--output-format`.

### Example

```bash
lang-sort ./kubejs/assets/kubejs/lang/en_us.json ./kubejs/assets/kubejs/lang/en_us_sorted.json
```
(Please note that if you output to a different file like `en_us_sorted.json`, you will need to rename it to `en_us.json` and overwrite the original file for the changes to be reflected in the game.)

```bash
lang-sort ./assets/examplemod/lang/en_us.lang ./assets/examplemod/lang/en_us_sorted.lang
```

## 📝 Dependencies
None.