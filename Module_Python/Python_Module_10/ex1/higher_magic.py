#!/usr/bin/env python3
from collections.abc import Callable


def spell(target: str, power: int) -> str:
    return (f"I summon intensity (power {power}) "
            f"and I direct it to {target}")


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(
        spell1: Callable[[str, int], str],
        spell2: Callable[[str, int], str]) -> Callable[
            [str, int], tuple[str, str]]:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(
        base_spell: Callable[[str, int], str],
        multiplier: int) -> Callable[[str, int], str]:
    return lambda target, power: base_spell(target, multiplier * power)


def conditional_caster(
        condition: Callable[..., str],
        spell: Callable[[str, int], str]) -> Callable[[str, int], str]:
    return lambda target, power: (
        spell(target, power) if condition(target, power) else "Spell fizzled"
    )


def spell_sequence(
        spells: list[Callable[[str, int], str]]
    ) -> Callable[[str, int], str]:
    res_spell: list[Callable[[str, int], int]] = []
    for spell in spells:
        res_spell.append(spell(str, int))


def main() -> None:
    test_values: list[int] = [22, 24, 5]
    test_targets: list[str] = ["Dragon", "Goblin", "Wizard", "Knight"]

    combined = spell_combiner(heal, spell)
    for value in test_values:
        for target in test_targets:
            res = combined(target, value)
    print(res)
    mega_fireball = power_amplifier(spell, 6)
    print(mega_fireball("Tax", 2))

    caster_invalid = conditional_caster(heal, heal)
    print(caster_invalid("Dragon", 10))

    liste = [heal, spell]
    s = spell_sequence(liste)



if __name__ == "__main__":
    main()
