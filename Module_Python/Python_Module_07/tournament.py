#!/usr/bin/env python3
from typing import Any
from ex2.battle_strategy import (
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
    InvalidStrategyError,
)
from ex0.fire import FlameFactory
from ex0.water import AquaFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory


def battle(opponents: list[tuple[Any, Any]]) -> None:
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_1, strategy_1 = opponents[i]
            factory_2, strategy_2 = opponents[j]

            creature_1 = factory_1.create_base()
            creature_2 = factory_2.create_base()

            print("\n* Battle *")
            print(creature_1.describe())
            print(" vs.")
            print(creature_2.describe())
            print(" now fight!")

            try:
                strategy_1.act(creature_1)
                strategy_2.act(creature_2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    battle([(FlameFactory(), normal), (HealingCreatureFactory(), defensive)])

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    battle(
        [
            (FlameFactory(), aggressive),
            (HealingCreatureFactory(), defensive),
        ]
    )
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    battle(
        [
            (AquaFactory(), normal),
            (HealingCreatureFactory(), defensive),
            (TransformCreatureFactory(), aggressive),
        ]
    )


if __name__ == "__main__":
    main()
