from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type_creature: str) -> None:
        self._name: str = name
        self._type: str = type_creature

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"
