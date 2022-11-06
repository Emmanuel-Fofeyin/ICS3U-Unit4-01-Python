#!/usr/bin/env python3

# Created by: Emmanuel
# Created on: Nov 2022
# This program uses a while loop


def main():
    # this function uses a while loop

    # this is to keep track of hw many times you go through the loop
    loop_counter = 0
    add_int = 0

    # input
    integer = input("Please enter a positive number: ")
    print("")

    # process & output
    try:
        integer = int(integer)
        if integer > 0:
            while loop_counter < integer:
                loop_counter = loop_counter + 1
                add_int = add_int + loop_counter
                print(
                    "The sum of all positive numbers from 1 to {0} is {1}.".format(
                        integer, add_int
                    )
                )
        else:
            print("{0} is not a positive integer".format(integer))
    except ValueError:
        print("{0} is not a valid input".format(integer))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
