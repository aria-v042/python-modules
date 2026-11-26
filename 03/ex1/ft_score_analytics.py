#!/usr/bin/env python3

import sys


def parse_input(argv: list[str]) -> list[int]:
    scores: list[int] = list()
    i: int = 0
    # TODO
    for arg in argv[1:]:
        try:
            scores[i] = int(arg)
        except ValueError as e:
            print(f"Invalid parameter: '{e}'")
        else:
            i += 1

    return scores


def main() -> int:
    print("=== Player Score Analytics ===")

    # av = sys.argv
    # ac = len(av)
    # if (ac < 2):
    #     print("No scores provided. Usage: python3 ft_score_analytics.py "
    #           "<score1> <score2> ...")
    #     return 0
    #
    scores: list[int] = parse_input(sys.argv)
    if (len(scores) == 0):
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return 0

    print("Scores processed:", scores)
    print("Total players:", len(scores))
    print("Total score:", sum(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", max(scores) - min(scores))

    return 0


if __name__ == "__main__":
    main()
