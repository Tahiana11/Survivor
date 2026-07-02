#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print("Program name: ", sys.argv[0])

    nbr_argv: int = len(sys.argv)
    if nbr_argv - 1 == 0:
        print("No arguments provided!")

    else:
        print("Arguments received: ", nbr_argv - 1)

        i: int = 1
        while i < nbr_argv:
            print("Argument ", i, ":", sys.argv[i])
            i += 1

    print("Total arguments: ", nbr_argv)
