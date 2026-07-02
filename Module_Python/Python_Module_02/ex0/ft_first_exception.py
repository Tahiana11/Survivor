#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/23 11:34:16 by mamy-and        #+#    #+#               #
#  Updated: 2026/04/30 20:44:30 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def input_temperature(temp_str: str) -> int:
    convert_str: int = int(temp_str)
    return (convert_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    list_str: list[str] = ["25", "abc"]

    for l_str in list_str:
        try:
            input_temperature(l_str)
            print(f"\nInput data is '{l_str}'")
            print(f"Temperature is now {l_str}°C")

        except ValueError as e:
            print(f"\nInput data is '{l_str}'")
            print("Caught input_temperature error:", e)


if __name__ == '__main__':
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
