# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/21 07:27:02 by mamy-and        #+#    #+#               #
#  Updated: 2026/03/21 07:27:25 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif (unit == "grams"):
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif (unit == "area"):
        print(f"{seed_type.capitalize()} seeds: covers {quantity}"
              f" square meters")
    else:
        print("Unknown unit type")
