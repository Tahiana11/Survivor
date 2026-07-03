#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/11 07:09:10 by mamy-and        #+#    #+#               #
#  Updated: 2026/04/16 11:29:40 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = height
        self._age: int = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"\nHeight updated: {self._height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected\n")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days\n")

    def show(self) -> None:
        print(
            f"{self.name}: "
            f"{round(self._height, 2)}cm, {self._age} days old"
        )


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.is_bloom: bool = False

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.is_bloom = True

    def display_state(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_bloom:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def show(self) -> None:
        print("=== Flower")
        self.display_state()
        self.bloom()
        self.display_state()


class Tree(Plant):
    def __init__(self, name: str, height: float, age:
                 int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self._height}cm"
              f" long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        print("\n=== Tree")
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: float) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvestseason(self) -> None:
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self, days: int, growth: float, value: int) -> None:
        print("[make tomato grow and age for 20 days]")
        self._height = self._height + growth
        self._age = self._age + days
        self.nutritional_value = self.nutritional_value + value
        super().show()
        self.harvestseason()

    def show(self) -> None:
        print("\n=== Vegetable")
        super().show()
        self.harvestseason()
        self.grow(20, 42.0, 20)


def main() -> None:
    print("=== Garden Plant Types ===")
    my_plant: list[Plant] = [
        Flower("Rose", 15.0, 10, "red"),
        Tree("Oak", 200.0, 365, 5.0),
        Vegetable("Tomato", 5.0, 10, "April", 0)
    ]
    for p in my_plant:
        p.show()


if __name__ == '__main__':
    main()
