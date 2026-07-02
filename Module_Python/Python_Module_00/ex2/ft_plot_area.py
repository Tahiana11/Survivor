# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plot_area.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mamy-and <mamy-and@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/13 10:22:09 by mamy-and        #+#    #+#               #
#  Updated: 2026/03/13 10:26:35 by mamy-and        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def ft_plot_area() -> None:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f"Plot area : {length * width}")
