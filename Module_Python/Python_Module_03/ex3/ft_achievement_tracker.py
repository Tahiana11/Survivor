#!/usr/bin/env python3
import random


def gen_player_achievements() -> set[str]:
    skills: list[str] = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
    ]

    nb: int = random.randint(4, len(skills) // 2)
    skill = set(random.sample(skills, nb))
    return skill


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    player: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }

    for n in player:
        print(f"Player {n}: {player[n]}")

    u: set[str] = set.union(*(player[n] for n in player))
    print(f"\nAll distinct achievements: {u}")

    i: set[str] = set.intersection(*(player[n] for n in player))
    print(f"\nCommon achievements: {i}")
    print()

    for n1 in player:
        n2: set[str] = set()
        for n3 in player:
            if n3 != n1:
                n2 = n2.union(player[n3])

        only = player[n1].difference(n2)
        print(f"Only {n1} has: {only}")

    print()
    for n in player:
        missing: set[str] = u.difference(player[n])
        print(f"{n} is missing: {missing}")


if __name__ == "__main__":
    main()
