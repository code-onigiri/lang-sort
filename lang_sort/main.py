import argparse
import sys
import json
from pathlib import Path
from .sorter import AnchorLangSorter


def detect_format(path: str, explicit_format: str = None) -> str:
    if explicit_format:
        return explicit_format

    ext = Path(path).suffix.lower()
    if ext == ".json":
        return "json"
    if ext == ".lang":
        return "lang"
    return "json"


def parse_lang_file(path: str) -> dict:
    data = {}
    with open(path, "r", encoding="utf-8-sig") as f:
        for line_num, raw_line in enumerate(f, start=1):
            line = raw_line.rstrip("\r\n")
            stripped = line.strip()

            if not stripped or stripped.startswith("#"):
                continue

            if "=" not in line:
                raise ValueError(f"Invalid .lang line {line_num}: '=' not found")

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            if not key:
                raise ValueError(f"Invalid .lang line {line_num}: empty key")

            data[key] = value

    return data


def dump_lang_text(sorted_entries: list) -> str:
    lines = []
    for key, value in sorted_entries:
        if key.startswith("__BLANK_LINE_"):
            lines.append("")
        else:
            lines.append(f"{key}={value}")
    return "\n".join(lines) + "\n"


def load_input_file(path: str, input_format: str) -> dict:
    if input_format == "json":
        with open(path, "r", encoding="utf-8-sig") as f:
            return json.load(f)
    return parse_lang_file(path)


def build_output_text(sorter: AnchorLangSorter, output_format: str) -> str:
    if output_format == "json":
        return sorter.sort_to_json_string()
    return dump_lang_text(sorter.sort_entries())

def main():
    parser = argparse.ArgumentParser(description="Smart sorter for Minecraft lang files.")
    parser.add_argument("input", help="Path to the input lang file (.json/.lang)")
    parser.add_argument("output", help="Path to the output sorted lang file (.json/.lang)")
    parser.add_argument(
        "--input-format",
        choices=["json", "lang"],
        default=None,
        help="Input format override (default: auto detect from extension)",
    )
    parser.add_argument(
        "--output-format",
        choices=["json", "lang"],
        default=None,
        help="Output format override (default: auto detect from extension)",
    )
    
    args = parser.parse_args()

    input_format = detect_format(args.input, args.input_format)
    output_format = detect_format(args.output, args.output_format)
    
    print(f"Reading language file: {args.input}")
    try:
        data = load_input_file(args.input, input_format)
    except FileNotFoundError:
        print(f"Error: Input file '{args.input}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{args.input}'.\nDetails: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Invalid LANG format in '{args.input}'.\nDetails: {e}")
        sys.exit(1)

    print("Clustering and sorting keys...")
    sorter = AnchorLangSorter(data)
    
    try:
        final_output_text = build_output_text(sorter, output_format)
    except Exception as e:
        print(f"An error occurred during processing: {e}")
        sys.exit(1)

    print(f"Writing sorted file to: {args.output}")
    try:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(final_output_text)
        print("Done! The language file has been successfully clustered and sorted.")
    except Exception as e:
        print(f"Error: Could not write to '{args.output}'.\nDetails: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()