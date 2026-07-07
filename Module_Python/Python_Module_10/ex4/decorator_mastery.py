#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any
import time
import functools
import random


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        begining = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - begining:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if len(args) > 2 and isinstance(args[0], MageGuild):
                power = args[2]
            elif len(args) > 1:
                power = args[0]

            if power >= min_power:
                return func(*args, **kwargs)

            else:
                return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(max_attemps: int) -> Callable[..., Any]:
    def retry_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attemps in range(1, max_attemps + 1):
                try:
                    return func(*args, **kwargs)

                except Exception:
                    return ("Spell failed, retrying... "
                            f"(attempt {attemps}/{max_attemps})")

            return ("Spell casting failed after "
                    f"{max_attemps} attemps")

        return wrapper
    return retry_decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (len(name) >= 3 and all(c.isalpha() or
                                       c.isspace() for c in name))

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(1.303)
    return "Fireball cast!"


@power_validator(min_power=50)
def heal(power: int, target: str) -> str:
    return f"Heal restores {target} for {power} HP"


@retry_spell(max_attemps=4)
def spell() -> str:
    if random.random() < 0.2:
        raise Exception("The spell missed its target!")
    return "Waaaaaaagh spelled !"


def main() -> None:
    print("Testing spell timer...")
    fire = fireball()
    print("Result:", fire)

    print("\nTesting retrying spell...")
    spells = spell()
    print(spells)

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("John Martin"))
    print(MageGuild.validate_mage_name(""))
    mage = MageGuild()
    powers = [15, 5]
    for power in powers:
        light = mage.cast_spell("Lightning", power)
        print(light)


if __name__ == "__main__":
    main()
