#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
from math import pi

# decoration
print(stylize("\n---- | Area angle converter | ----\n", fg("red")))

# class
class AAConverter:
    def __init__(self, choice, value):
        self.choice = choice
        self.value = value

    # output magic method
    def __repr__(self):
        if self.choice == "R":
            radian_val = stylize(self.to_radian(self.value), fg("red"))
            return f"{self.value} ° is {radian_val} rad.\n"
        elif self.choice == "D":
            degree_val = stylize(self.to_degree(self.value), fg("red"))
            return f"{self.value} rad is {degree_val} °.\n"
        else:
            exit("\nInvalid Input\n")

    # methods
    def to_degree(self, val):
        return str(round(val * 180 / pi, 3))

    def to_radian(self, val):
        return str(round(val * pi / 180, 3))

# main execution
if __name__ == "__main__":
    # options
    print(stylize("Options:", fg("green")))
    print("'R' for radian output type\n'D' for degree output type\n")

    # user interaction
    choice = input(": ").upper()
    value = float(input("\nValue: "))

    print(AAConverter(choice, value))
