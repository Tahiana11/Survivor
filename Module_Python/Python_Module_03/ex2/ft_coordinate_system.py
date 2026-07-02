#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        enter = input("Enter new coordinates as floats in format 'x,y,z': ")
        values: list[str] = enter.split(",")

        try:
            x, y, z = values

        except ValueError:
            print("Invalid syntax")
            continue

        coords: list[float] = []
        for p in (x, y, z):
            try:
                coords += [float(p.strip())]

            except ValueError:
                print(
                    f"Error on parameter '{p}': could not convert"
                    f" string to float: '{p}'"
                )
                break

        else:
            return (coords[0], coords[1], coords[2])


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    distance1: float = math.sqrt(pos1[0] ** 2 + pos1[1] ** 2 + pos1[2] ** 2)
    print(f"Distance to center: {round(distance1, 4)}")

    print("\nGet a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()
    distance2: float = math.sqrt(
        (pos2[0] - pos1[0]) ** 2 +
        (pos2[1] - pos1[1]) ** 2 +
        (pos2[2] - pos1[2]) ** 2
    )
    print(f"Distance between the 2 sets of coordinates: {round(distance2, 4)}")


if __name__ == "__main__":
    main()
