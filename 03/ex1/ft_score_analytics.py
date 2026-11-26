#!/usr/bin/env python3

import sys


def parse_input(av: list[str]) -> list[str]:
    scores = []
    for arg in av[1:]:
        try:
            score = int(arg)
        except ValueError as e:
            print(f"Invalid parameter: '{e}'")



def main() -> int:
    print("=== Player Score Analytics ===")

    av = sys.argv
    ac = len(av)

    if (ac < 2):
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return 0

    parse_input(av)

    return 0


if __name__ == "__main__":
    main()
