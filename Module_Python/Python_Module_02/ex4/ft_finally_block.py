#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/28 20:58:42 by mamy-and        #+#    #+#               #
#  Updated: 2026/05/04 15:13:38 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class GardenError(Exception):
    def __init__(
        self, message: str = "A general garden error occurred"
    ) -> None:
        self.message: str = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknow plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unkown error(water)") -> None:
        super().__init__(message)


def CheckWaterError(water: int) -> None:
    if water < 2:
        raise WaterError("Not enough water in the tank!")
    print("Sufficient water level in the tank!")


def water_plant(plant_name: str) -> None:
    name: str = plant_name.capitalize()
    if plant_name != name:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    print("Opening watering system")
    plants: list[str] = ["Tomato", "Lettuce", "Carrots"]
    try:
        for p in plants:
            water_plant(p)

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        return

    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")
    invalid_plants: list[str] = ["Lawyer", "lettuce", "Avocat"]
    try:
        for p in invalid_plants:
            water_plant(p)

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
