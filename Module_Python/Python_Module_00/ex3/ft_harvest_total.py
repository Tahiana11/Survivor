# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/21 07:11:52 by mamy-and        #+#    #+#               #
#  Updated: 2026/03/30 07:47:27 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def ft_harvest_total() -> None:
    total: int = 0
    day: int = 1
    while (day < 4):
        a = input(f"Day {day} harvest: ")
        total += int(a)
        day += 1
    print(f"Total harvest: {total}")
