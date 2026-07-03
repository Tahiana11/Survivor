#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()
    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def battle(flame_factory: FlameFactory, aqua_factory: AquaFactory) -> None:
    print("Testing battle")
    flame_creature = flame_factory.create_base()
    aqua_creature = aqua_factory.create_base()
    print(flame_creature.describe())
    print(" vs.")
    print(aqua_creature.describe())
    print(" fight!")
    print(flame_creature.attack())
    print(aqua_creature.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    print()
    battle(flame_factory, aqua_factory)
