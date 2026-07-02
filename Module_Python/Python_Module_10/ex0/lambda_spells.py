#!/usr/bin/env python3
from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda p: p["power"], reverse=True)


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: " * " + spell + " * ", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    max_power = max(mages, key=lambda mage: mage["power"])
    min_power = min(mages, key=lambda mage: mage["power"])
    power = list(map(lambda m: m["power"], mages))
    avg_power = sum(power) / len(power)
    return {
            "max_power": max_power["power"],
            "min_power": min_power["power"],
            "avg_power": round(avg_power, 2)}


def main() -> None:
    print("Testing artifact sorter...")
    artifacts: list[dict[str, Any]] = [
        {'name': 'Wind Cloak', 'power': 63, 'type': 'focus'},
        {'name': 'Shadow Blade', 'power': 66, 'type': 'weapon'},
        {'name': 'Earth Shield', 'power': 93, 'type': 'weapon'},
        {'name': 'Shadow Blade', 'power': 70, 'type': 'weapon'}
    ]
    artifact_sorted = artifact_sorter(artifacts)
    print(artifact_sorted[0]["name"], artifact_sorted[0]["type"], "(", end="")
    print(artifact_sorted[0]["power"], "power) comes before ", end="")
    print(artifact_sorted[1]["name"], artifact_sorted[1]["type"], "(", end="")
    print(artifact_sorted[1]["power"], "power)")

    print()
    print("Testing spell transformer...")
    spells: list[str] = ["meteor", "earthquake", "freeze", "lightning"]
    print(" ".join(spell_transformer(spells)))

    print()
    print("Testing power filter...")
    mages: list[dict[str, Any]] = [
        {"name": "Morgan", "power": 58, "element": "wind"},
        {"name": "Phoenix", "power": 56, "element": "lightning"},
        {"name": "Rowan", "power": 99, "element": "wind"},
        {"name": "Rowan", "power": 75, "element": "water"},
        {"name": "Phoenix", "power": 60, "element": "lightning"},
    ]
    power: list[dict[str, Any]] = power_filter(mages, 90)
    print("List of powerful Mages:")
    for p in power:
        print(" - ", p["name"])

    print()
    print("Mage stats...")
    stats: dict[str, Any] = mage_stats(mages)
    print("Max:", stats["max_power"])
    print("Min:", stats["min_power"])
    print("Average:", stats["avg_power"])


if __name__ == "__main__":
    main()
