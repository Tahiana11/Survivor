# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/21 07:24:24 by mamy-and        #+#    #+#               #
#  Updated: 2026/03/30 08:28:22 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def ft_count_harvest_recursive() -> None:
    day = input("Days until harvest: ")
    day = int(day)

    def ft_recursive(computer: int) -> None:
        if (computer > day):
            print("Harvest time!")
            return
        print(f"Day {computer}")
        ft_recursive(computer + 1)
    ft_recursive(1)
