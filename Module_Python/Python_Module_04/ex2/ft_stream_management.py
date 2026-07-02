#!/usr/bin/env python3
import sys
from typing import IO


def read_file(file: IO[str]) -> str:
    content: str = file.read()
    return content


def open_file(file: str) -> IO[str]:
    print(f"Accessing file '{file}'")
    content: IO[str] = open(file, "r")
    return content


def transform_data(content: str) -> None:
    print("\nTransform data:")
    print("---\n")
    lines: list[str] = content.splitlines()
    new_content = ""
    for line in lines:
        if line != "":
            new_content += line + "#\n"

    print(new_content)
    print("---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    name_file: str = sys.stdin.readline().strip()
    if name_file == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{name_file}'")
        try:
            new_file = open(name_file, "w")
            try:
                new_file.write(new_content)
            except Exception as e:
                print(f"Error while writing : {e}", file=sys.stderr)
                print("Not saving data.")
            finally:
                new_file.close()

        except Exception as e:
            print(f"[STDERR] Error opening file '{name_file}': "
                  f"{e}\n", file=sys.stderr)


def main() -> None:
    script: str = sys.argv[0]
    if len(sys.argv) != 2:
        print(f"Usage: {script} <file>")

    else:
        print("=== Cyber Archives Recovery  & Preservation ===")

        file: str = sys.argv[1]
        try:
            fl: IO[str] = open_file(file)
            try:
                print("---\n")
                content: str = read_file(fl)
                print(content)
                print("---")

            finally:
                fl.close()
                print(f"File '{file}' closed.")

            transform_data(content)

        except Exception as e:
            print(f"Error opening file '{file}': {e}\n", file=sys.stderr)


if __name__ == "__main__":
    main()
