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
            print("{} is not a valid number".format(user_number))
        else:

            # Initialize power variable
            power_of_two = 1

            # Calculate the power of two of the number inputted by the user
            for counter in range(user_number_int):
                print("Tracking {} times through the loop".format(counter))
                power_of_two = power_of_two * 2

            # Display power of two to user
            print("The power of two of {} is {}".format(user_number_int, power_of_two))
    except ValueError:
        print("{} is not a valid number".format(user_number))


if __name__ == "__main__":
    main()
