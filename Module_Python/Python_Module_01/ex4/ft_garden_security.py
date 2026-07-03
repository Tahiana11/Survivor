#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/11 07:08:58 by mamy-and        #+#    #+#               #
#  Updated: 2026/04/21 06:47:35 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class Plant():
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
        print(f"Current state: {self.name}: "
              f"{self._height:.1f}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")
    s_height: float = 15.0
    s_age: int = 10
    p = Plant("Rose", s_height, s_age)
    print(f"Plant created: {p.name}: {s_height}cm, {s_age} days old")
    p.set_height(25)
    p.set_age(30)
    p.set_height(-1)
    p.set_age(-1)
    p.show()


if __name__ == '__main__':
    main()
