#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/11 07:09:23 by mamy-and        #+#    #+#               #
#  Updated: 2026/04/21 06:52:32 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._show_plant: int = 0
            self._growth: int = 0
            self._old_age: int = 0

        def display(self) -> None:
            print(
                f"Stats: {self._growth} grow, {self._old_age} age,"
                f" {self._show_plant} show"
            )

        def increase_grow(self) -> None:
            self._growth += 1

        def increase_age(self) -> None:
            self._old_age += 1

        def increase_show(self) -> None:
            self._show_plant += 1

    def __init__(self, name: str, height: float, older: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_days: int = older
        self.stats = self._Stats()

    @staticmethod
    def age_verify(days: int) -> bool:
        is_more_than_year = days >= 365
        print(f"Is {days} days more than a year? -> {is_more_than_year}")
        return is_more_than_year

    def grow(self, height: float) -> None:
        self.stats.increase_grow()
        self.height += height

    def age(self, days: int) -> None:
        self.stats.increase_age()
        self.age_days += days

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        self.stats.increase_show()
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


class Flower(Plant):
    def __init__(
            self, name: str, height: float, older: int, color: str
    ) -> None:
        self.color: str = color
        super().__init__(name, height, older)
        self.is_bloom: bool = False

    def bloom(self) -> None:
        self.is_bloom = True

    def display_state(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_bloom:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def grow(self, height: float) -> None:
        super().grow(height)

    def age(self, days: int) -> None:
        super().age(days)

    def show_flower(self) -> None:
        print("\n=== Flower")
        self.display_state()
        self.bloom()
        show_statics(self)
        print("[asking the rose to grow and bloom]")
        self.grow(8.0)
        self.display_state()

    def show(self) -> None:
        self.show_flower()


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter
        self.shade: int = 0

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of {self.height}cm"
            f" long and {self.trunk_diameter}cm wide."
        )
        self.shade += 1

    def show_Tree(self) -> None:
        print("\n=== Tree")
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")
        show_statics(self)
        print(f" {self.shade} shade")
        self.produce_shade()
        show_statics(self)
        print(f" {self.shade} shade")

    def show(self) -> None:
        self.show_Tree()


class Seed(Flower):
    seeds: int = 0

    def __init__(
        self, name: str, height: float, age: int, color: str, seeds: int
    ) -> None:
        super().__init__(name, height, age, color)
        self.seeds = seeds

    def bloom(self) -> None:
        self.is_bloom = True
        self.seeds = 42

    def show_Seed(self) -> None:
        print("\n=== Seed")
        self.display_state()
        print(f" Seeds: {self.seeds}")
        print("[make sunflower grow, age and bloom]")
        self.grow(30.0)
        self.age(20)
        self.bloom()
        self.display_state()
        print(f" Seeds: {self.seeds}")

    def show(self) -> None:
        self.show_Seed()


def show_statics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


def main() -> None:
    print("=== Garden statistics ===")
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)

    print("=== Check year-old ===")
    Plant.age_verify(30)
    Plant.age_verify(400)

    rose.show()
    show_statics(rose)

    oak.show()

    sunflower.show()
    show_statics(sunflower)

    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    show_statics(anonymous)


if __name__ == "__main__":
    main()
