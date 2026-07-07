#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: '{operation}'."
                         f" Expected one of {list(operations.keys())}.")

    return functools.reduce(operations[operation], spells)


def enchantment(power: int, element: str, target: str) -> str:
    return f"{target} receives a {element} enchantment of power {power}."


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    return {
        "fire": functools.partial(base_enchantment, 50, "Fire"),
        "water": functools.partial(base_enchantment, 50, "Water"),
        "earth": functools.partial(base_enchantment, 50, "Earth")
    }


@functools.lru_cache(maxsize=1)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(spells: Any) -> str:
        return "Unknwon spell type"

    @dispatcher.register
    def _(spells: int) -> str:
        return f"{spells} damage"

    @dispatcher.register
    def _(spells: str) -> str:
        return f"{spells}"

    @dispatcher.register(list)
    def _(spells: list[Any]) -> str:
        return f"{len(spells)} spells"

    return dispatcher


def main() -> None:
    print("Testing spell reducer...")
    spells: list[int] = [60, 25, 39, 47]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))

    print("\nTesting memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print("Damage spell:", dispatcher(42))
    print("Enchantment:", dispatcher("Fireball"))
    print("Multi-cast:", dispatcher(["Fireball", "Ice", "Wind"]))
    print(dispatcher(10.8))


if __name__ == "__main__":
    main()
