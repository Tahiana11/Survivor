#!/usr/bin/env python3
import sys
import os
import site


def is_virtual() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if not is_virtual() or "VIRTUAL_ENV" not in os.environ:
        print("MATRIX STATUS: You're still plugged in")

        print("\nCurrent Python:", sys.executable)
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\\Scripts\\activate # On Windows")

        print("\nThen run this program again.")

    else:
        print("MATRIX STATUS: Welcome to the construct")

        print("\nCurrent Python:", sys.executable)
        print("Virtual Environment:", os.path.basename(sys.prefix))
        print("Environment Path:", sys.prefix)

        print("\nSUCCESS: You're in an isolated environment!"
              "\nSafe to install packages without affecting the"
              " global system.")

        paths = site.getsitepackages()
        if paths:
            print("\nPackages installation path:", paths[0])
        else:
            print("\nNot found")


if __name__ == "__main__":
    main()
