# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/21 07:20:17 by mamy-and        #+#    #+#               #
#  Updated: 2026/03/30 07:55:07 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def ft_water_reminder() -> None:
    last_water = int(input("Days since last watering: "))
    if (last_water > 2):
        print("Water the plants!")
    elif (last_water <= 2):
        print("Plants are fine")
