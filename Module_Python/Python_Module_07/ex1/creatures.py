from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class Sproutling(HealCapability, Creature):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"


class Bloomelle(HealCapability, Creature):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def heal(self) -> str:
        return f"{self._name} heals itself and others for a large amount"

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        TransformCapability.__init__(self)
        Creature.__init__(self, "Shiftling", "Normal")

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self._name} performs a boosted strike!"
        return f"{self._name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self._name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        TransformCapability.__init__(self)
        Creature.__init__(self, "Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self._name} unleashes a devastating morph strike!"
        return f"{self._name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self._name} stabilizes its form."
