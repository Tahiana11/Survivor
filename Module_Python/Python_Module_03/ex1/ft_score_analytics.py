#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    arguments: list[str] = sys.argv[1:]
    nbr_argv: int = len(sys.argv)
    total: int = 0

    try:
        if nbr_argv < 2:
            raise IndexError("python3 ft_score_analytics.py "
                             "<score1> <score2> ...")

        list_scores: list[int] = []
        for arg in arguments:
            try:
                value: int = int(arg)
                list_scores += [value]
                total += 1

            except ValueError:
                print(f"Invalid parameter: '{arg}'")

        if len(list_scores) < 1:
            raise IndexError("python3 ft_score_analytics.py "
                             "<score1> <score2> ...")

        if list_scores:
            print("Scores processed: ", list_scores)
            print("Total players:", total)
            print("Total score:", sum(list_scores))
            print("Average score:", sum(list_scores) / total)
            print("High score:", max(list_scores))
            print("Low score:", min(list_scores))
            print("Score range:", max(list_scores) - min(list_scores))

    except IndexError as e:
        print("No scores provided. Usage:", e)


if __name__ == "__main__":
    main()
