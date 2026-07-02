from alchemy.elements import create_air, create_earth
import elements


def healing_potion() -> str:
    return ("Healing potion brewed with "
            f"'{create_earth()}' and '{create_air()}'")


def strength_potion() -> str:
    return ("Strength potion brewed with "
            f"'{elements.create_fire()}' and '{elements.create_water()}'")
