#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    counter: int = 0

    def increment() -> int:
        nonlocal counter
        counter += 1
        return counter

    return increment


def spell_accumulator(initial_power: int) -> Callable[..., int]:
    def addition(add: int) -> int:
        nonlocal initial_power
        initial_power += add
        return initial_power

    return addition


def enchantment_factory(enchantment_type: str) -> Callable[..., str]:
    def enchantement(name: str) -> str:
        return f"{enchantment_type} {name}"

    return enchantement


def memory_vault() -> dict[str, Callable[..., Any | None]]:
    storage: dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:
        storage[key] = value

    def recall(key: Any) -> Any:
        return storage.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall,
    }


def main() -> None:
    initial_powers = [31, 71]
    power_additions = [15, 11]
    enchantment_types = ['Shocking', 'Earthen', 'Flowing']
    items_to_enchant = ['Wand', 'Staff', 'Shield', 'Cloak']

    print("Testing mage counter...")
    counter_a = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_a call 3:", counter_a())
    counter_b = mage_counter()
    print("counter_b call 1:", counter_b())

    print("\nTesting spell accumulator...")
    for power in initial_powers:
        for add in power_additions:
            for add1 in power_additions:
                if add != add1:
                    add_accumulator = spell_accumulator(power)
                    print(f"Base {power}, add {add1}:", add_accumulator(add1))
                    print(f"Base {power}, add {add}:", add_accumulator(add))
                    print()

    print("Testing enchantment factory...")
    enchantment = enchantment_factory(enchantment_types[1])
    print(enchantment(items_to_enchant[2]))
    enchantment = enchantment_factory(enchantment_types[2])
    print(enchantment(items_to_enchant[0]))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret'= 42")
    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'unknwon':", vault["recall"]("unknwon"))


if __name__ == "__main__":
    main()
