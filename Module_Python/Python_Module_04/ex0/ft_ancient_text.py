#!/usr/bin/env python3
import sys
from typing import IO


def read_file(f: IO[str]) -> str:
    content: str = f.read()
    return (content)


def open_file(f: str) -> IO[str]:
    print(f"Accessing file '{f}'")
    file: IO[str] = open(f, "r")
    return (file)


def main() -> None:
    script: str = sys.argv[0]
    if len(sys.argv) != 2:
        print(f"Usage: {script} <file>")

    else:
        print("=== Cyber Archives Recovery ===")

        file: str = sys.argv[1]
        try:
            f: IO[str] = open_file(file)
            try:
                print("---\n")
                r: str = read_file(f)
                print(r)
                print("---")

            finally:
                f.close()
                print(f"File '{file}' closed.")

        except (Exception) as e:
            print(f"Error opening file '{file}': {e}")


if __name__ == "__main__":
    main()
