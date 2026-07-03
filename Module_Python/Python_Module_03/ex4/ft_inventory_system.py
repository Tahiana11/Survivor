#!/usr/bin/env python3
import sys


def main() -> None:
    inventory: dict[str, int] = {}
    print("=== Inventory System Analysis ===")

    if not sys.argv[1:]:
        print(
            "Error ... the format is: python3"
            " ft_inventory_system.py <item_name>:<quantity>"
        )
        return

    for a in sys.argv[1:]:
        if ":" not in a:
            print(f"Error - invalid parameter '{a}'")
            continue

        p = a.split(":", 1)
        if p[0] == "" or p[1] == "":
            print(f"Error - invalid parameter '{a}'")
            continue

        item_name = p[0]
        try:
            quantity: int = int(p[1])
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
            continue

        if quantity <= 0:
            print(
                f"Quantity error for '{item_name}': "
                f"must be a positive integer, got {quantity}"
            )
            continue

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
        else:
            inventory[item_name] = quantity

    if not inventory:
        print("No valid items were added to the inventory.")
        return

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)}"
          f" items: {sum(inventory.values())}")

    sum_inventory: int = sum(inventory.values())
    for k in inventory.keys():
        try:
            j: float = inventory[k] * 100 / sum_inventory
            print(f"Item {k} represents {round(j, 1)}%")
        except ZeroDivisionError:
            return

    k_max = k_min = list(inventory)[0]
    for k in inventory:
        if inventory[k] > inventory[k_max]:
            k_max = k
        if inventory[k] < inventory[k_min]:
            k_min = k

    print(f"Item most abundant: {k_max} with quantity {inventory[k_max]}")
    print(f"Item least abundant: {k_min} with quantity {inventory[k_min]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
