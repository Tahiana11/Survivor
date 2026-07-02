#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 15:20:08 by mamy-and        #+#    #+#               #
#  Updated: 2026/06/02 14:16:13 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class GardenError(Exception):
    def __init__(
        self, message: str = "A general garden error occurred"
    ) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknow plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unkown error(water)") -> None:
        super().__init__(message)


def CheckWaterError(water: int) -> None:
    if (water < 2):
        raise WaterError("Not enough water in the tank!")
    print("Sufficient water level in the tank!")


def CheckPlantError(name: str, plant: str) -> None:
    if (plant == "wilt"):
        raise PlantError(f"The {name} plant is wilting!")
    print(f"The {plant} plant doesn't wilt!")


def check() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError..")
    try:
        CheckPlantError("tomate", "wilt")

    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        CheckWaterError(water=1)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        CheckPlantError("tomato", "wilt")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        CheckWaterError(water=1)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    check()
