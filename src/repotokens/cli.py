from argparse import ArgumentParser
from pathlib import Path

import tiktoken 

def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding("o200k_base")
    num_tokens = len(encoding.encode(string, disallowed_special=()))
    return num_tokens

def count_tokens(path_to_directory: str) -> str:
    path = Path(path_to_directory)
    total_tokens = 0
    for file_path in path.rglob("*"):
        if not file_path.is_dir():
            try:
                text = file_path.read_text(encoding="utf-8")
                total_tokens += num_tokens_from_string(text)
            except UnicodeDecodeError:
                pass
    return f"Token estimate: {total_tokens}"

def argument_parser():
    parser = ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    return args.path

def main():
    print(count_tokens(argument_parser()))

if __name__ == "__main__":
    main()