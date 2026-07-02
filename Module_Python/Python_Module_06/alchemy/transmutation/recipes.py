from alchemy.elements import create_air
from .. import potions
import elements


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew {create_air()} and"
        f" '{potions.strength_potion()}' mixed with '{elements.create_fire()}'"
    )
