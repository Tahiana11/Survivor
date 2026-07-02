# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/21 07:23:18 by mamy-and        #+#    #+#               #
#  Updated: 2026/03/31 06:56:04 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def ft_count_harvest_iterative():
    computer: int = 1
    day = int(input("Days until harvest: "))
    while (computer <= day):
        print(f"Day {computer}")
        computer += 1
    print("Harvest time!")
