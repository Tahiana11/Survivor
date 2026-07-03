#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 07:38:07 by mamy-and        #+#    #+#               #
#  Updated: 2026/05/04 09:32:39 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def input_temperature(temp_str: str) -> int | None:
    convert_str = int(temp_str)

    if convert_str > 40:
        raise ValueError(f"{convert_str}°C"
                         " is too hot for plants (max 40°C)")

    elif convert_str < 0:
        raise ValueError(f"{convert_str}°C"
                         " is too cold for plants (min 0°C)")

    else:
        return convert_str


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    list_str = ["25", "abc", "100", "-50", "abc10"]

    for l_str in list_str:
        try:
            temp = input_temperature(l_str)
            print(f"\nInput data is '{temp}'")
            print(f"Temperature is now {temp}°C")

        except ValueError as e:
            print(f"\nInput data is '{l_str}'")
            print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
