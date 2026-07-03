#!/usr/bin/env python3
from collections.abc import Callable


def spell(target: str, power: int) -> str:
    return (f"I summon intensity (power {power}) "
            f"and I direct it to {target}")


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power + 40} HP"


def has_enough_power(target: str, power: int) -> bool:
    return power > 0


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str],
) -> Callable[[str, int], tuple[str, str]]:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int,
) -> Callable[[str, int], str]:
    return lambda target, power: base_spell(target, multiplier * power)


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell_fn: Callable[[str, int], str],
) -> Callable[[str, int], str]:
    return lambda target, power: (
        spell_fn(target, power) if condition(target, power)
        else "Spell fizzled"
    )


def spell_sequence(
    spells: list[Callable[[str, int], str]],
) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]

    return sequence


def main() -> None:
    test_values: list[int] = [22, 24, 5]
    test_targets: list[str] = ["Dragon", "Goblin", "Wizard", "Knight"]

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result1, result2 = combined(test_targets[0], test_values[1])
    print("Combined spell result:", result1, ",", result2)

    print("\nTesting power amplifier...")
    amplified = power_amplifier(heal, 2)
    print("Original:", heal(test_targets[1], test_values[1]), end=", ")
    print("Amplified:", amplified(test_targets[1], test_values[1]))

    print("\nConditional spellcaster test...")
    conditional = conditional_caster(has_enough_power, fireball)
    print("Respect conditional:", conditional(test_targets[2], test_values[2]))

    print("\nTest spell sequence...")
    spells_to_cast: list[Callable[[str, int], str]] = [heal, spell, fireball]
    results = spell_sequence(spells_to_cast)(test_targets[3], test_values[1])
    print("Spell sequence:")
    for result in results:
        print(" - ", result)


if __name__ == "__main__":
    main()
