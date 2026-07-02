# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/21 07:18:12 by mamy-and        #+#    #+#               #
#  Updated: 2026/03/26 02:19:23 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plant_age() -> None:
    age = int(input("Enter plant age in days: "))
    if (age > 60):
        print("Plant is ready to harvest!")
    if (age <= 60):
        print("Plant needs more time to grow.")
