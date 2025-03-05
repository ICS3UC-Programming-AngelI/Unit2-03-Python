#!/usr/bin/env python3
# Created by: Angel
# Created on: Feb 03,2025
# This program asks the user for the diameter and radius of
# the pizza. It then calculates and displays the area and
# perimeter of the pizza.
import constants


def main():
    # get the diameter and radius the from user
    diameter = int(input("Enter the diameter of the pizza (inches): "))
    radius = int(input("Enter the radius of the pizza (inches): "))

    # calculates area and perimeter and the cost
    area = math.pi * radius * 2
    perimeter = 2 * math.pi * radius
    cost = diameter * 1.5 + 2.00 + 2.25 + (tax * (diameter * 1.5 + 2.00 + 2.25))

    # display the area, perimeter and the cost
    print("")
    print("Area = {} cm^2", format(area))
    print("Perimeter = {}cm".format(perimeter))
    print("cost = {cost:.2f}$".format(cost))


if __name__ == "__main__":
    main()
