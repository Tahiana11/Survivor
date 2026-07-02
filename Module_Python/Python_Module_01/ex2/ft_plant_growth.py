#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/11 07:08:39 by mamy-and        #+#    #+#               #
#  Updated: 2026/04/13 07:06:33 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_day: int = age

    def grow(self, daily_growth: float) -> None:
        self.height += daily_growth

    def age(self) -> None:
        self.age_day += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm,"
              f" {self.age_day} days old")

    def get_diff(self, height: float) -> float:
        return self.height - height


def main() -> None:
    print("=== Garden Plant Growth ===")
    height_init: float = 25.0
    day: int = 7
    daily_growth: float = 0.8
    age_p: int = 30
    rose = Plant("Rose", height_init, age_p)
    rose.show()
    i: int = 1
    while i <= day:
        print(f"=== Day {i} ===")
        rose.grow(daily_growth)
        rose.age()
        rose.show()
        i += 1
    grow = rose.get_diff(height_init)
    print(f"Growth this week: {grow:.1f}cm")


if __name__ == "__main__":
    main()
