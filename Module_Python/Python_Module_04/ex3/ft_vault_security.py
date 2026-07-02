#!/usr/bin/env python3
def secure_archive(action: str, file: str) -> tuple[bool, str]:
    data: str = ""
    try:
        if action == "r":
            with open(file, "r") as f:
                data = f.read()

        elif action == "w":
            with open(file, "w") as f:
                f.write("tata")
                data = "Content successfully written to file"

        elif action == "x":
            with open(file, "x") as f:
                f.write("tata")
                data = "Content successfully written to file"

        return (True, data)

    except Exception as e:
        return (False, f"{e}")


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("r", "/not/existing/file"))

    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("r", "/etc/shadow"))

    print()

    print("Using 'secure_archive' to creat a file:")
    print(secure_archive("x", "file.txt"))

    print()

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("r", "ancient_fragment.txt"))

    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("w", "f.txt"))


if __name__ == "__main__":
    main()
