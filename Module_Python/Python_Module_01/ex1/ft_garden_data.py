#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/11 07:08:25 by mamy-and        #+#    #+#               #
#  Updated: 2026/04/13 07:05:15 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_day: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm,"
              f" {self.age_day} days old")


def main() -> None:
    list_plant: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    print("=== Garden Plant Registry ===")
    for my_plant in list_plant:
        my_plant.show()


if __name__ == "__main__":
    main()
