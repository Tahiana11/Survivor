#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/11 07:08:48 by mamy-and        #+#    #+#               #
#  Updated: 2026/04/13 07:06:53 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_day: int = age

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age_day} days old"

    def grow(self, height: int) -> None:
        self.height += height


def main() -> None:
    print("=== Plant Factory Output ===")
    created: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]
    for plant in created:
        print("Created:", plant.show())


if __name__ == "__main__":
    main()
