#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    player: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "Emma",
        "john",
        "kevin",
        "Liam",
        "Gregory",
        "Dylan",
        "Larra"
    ]

    pl: list[str] = random.sample(player, k=len(player))
    print("Initial list of players", pl)

    capitalize_player: list[str] = [i.capitalize() for i in pl]
    print(f"New list with all names capitalized: {capitalize_player}")

    only_capitalize: list[str] = [p for p in player if p == p.capitalize()]
    print(f"New list of capitalized names only:{only_capitalize}")

    score: dict[str, int] = {
        name: random.randint(50, 1000) for name in capitalize_player
    }
    print(f"\nScore dict: {score}")

    total_score: int = 0
    for name in score:
        total_score += score[name]
    average: float = total_score / len(score)
    print(f"Score average is {round(average, 2)}")

    high: dict[str, int] = {
       name: score[name] for name in score if score[name] > average
    }
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()
