# module -> mass
# fuel for a module = round_down(m / 3) - 2

"""
The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel
required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take
its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for
the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
"""

import pathlib


def main(input_dir: str):
    input_path = pathlib.Path(input_dir)

    with input_path.open('r') as input_file:
        mass = input_file.readline()

        total_fuel = 0

        while mass:
            total_fuel += int(float(mass) / 3) - 2
            mass = input_file.readline()

    print(total_fuel)


if __name__ == "__main__":
    main('inputs/1.1.txt')
