#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/24 09:15:55 by mamy-and        #+#    #+#               #
#  Updated: 2026/04/30 16:54:00 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        x: int = int("abc10")
        print(x)

    elif operation_number == 1:
        b: int = 0
        a: float = 10 / b
        print(a)

    elif operation_number == 2:
        open("/non/existent/file", "w")

    elif operation_number == 3:
        s: str = "f" + 10
        print(s)

    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    i: int = 0
    while i <= 4:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)

        except ValueError as e:
            print("Caught ValueError:", e)

        except ZeroDivisionError as e:
            print("Caught ZeroDivisionError:", e)

        except FileNotFoundError as e:
            print("Caught FileNotFoundError:", e)

        except TypeError as e:
            print("Caught TypeError: ", e)

        i += 1

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
