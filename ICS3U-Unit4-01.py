#!/usr/bin/env python3

# Created by: Emmanuel
# Created on: Nov 2022
# This program uses a while loop


def main():

    loop_counter = 0
    add_int = 0

    # This function adds all the whole numbers up to the inputted number

    # Input
    positive_string = input("Enter a positive integer: ")
    print("")

    # Process and output
    try:
        positive_integer = int(positive_string)
        if positive_integer > 0:
            while loop_counter < positive_integer:
                loop_counter = loop_counter + 1
                add_int = add_int + loop_counter
            print(
                "The sum of all positive numbers from 1 to {0} is {1}.".format(
                    positive_integer, add_int
                )
            )
        else:
            print("{0} is not a positive integer".format(positive_string))
    except ValueError:
        print("{0}, is not a valid input".format(positive_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
