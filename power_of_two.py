#!/usr/bin/env python3
# Created By: Bryson Grant
# Date: 11 13, 2026
# This program gets a number from the user and displays the power of two of that number
# using a for loop


def main():
    # Get number from user
    user_number = input("Enter a number: ")
    # See if number inputted is a string
    try:
        user_number_int = int(user_number)
        if user_number_int < 0:
            print("{} is not a whole number integer".format(user_number))
        else:

            # Initialize power variable
            power_of_two = 1

            # Calculate the number to the power of two of the number inputted by the user
            for counter in range(user_number_int + 1):
                print("{}^2 = {}".format(counter, counter**2))
                power_of_two = counter**2

            # Display the number to the power of two to the user
            print(
                "The number {} raised to the power of two is {}".format(
                    user_number_int, power_of_two
                )
            )
    except ValueError:
        print("{} is not a whole number integer".format(user_number))


if __name__ == "__main__":
    main()
