#!/usr/bin/env python3

import sys


def main() -> int:
    print("=== Command Quest ===")

    print(f"Program name: {sys.argv[0]}")

    argv = sys.argv
    argc = len(argv)
    if (argc > 1):
        print(f"Arguments received: {argc - 1}")
        for i in range(1, argc):
            print(f"Argument {i}: {argv[i]}")
        # for arg in argv[1:]:
        #     print(f"Argument {argv.index(arg)}: {arg}")
    else:
        print("No arguments provided!")

    print(f"Total arguments: {argc}")
    return 0


if __name__ == "__main__":
    main()
