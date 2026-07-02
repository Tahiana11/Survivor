#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_factory(healing_factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base_creature = healing_factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.heal())
    print(" evolved:")
    evolved_creature = healing_factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.heal())


def test_transform_factory(
        transform_factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    base_creature = transform_factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.attack())
    print(base_creature.revert())
    print(" evolved:")
    evolved_creature = transform_factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.transform())
    print(evolved_creature.attack())
    print(evolved_creature.revert())


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    test_healing_factory(healing_factory)
    print()
    test_transform_factory(transform_factory)
