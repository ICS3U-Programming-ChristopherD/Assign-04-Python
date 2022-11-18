#!/usr/bin/env python3

# Created by: Chris Di Bert
# Date: Nov.18, 2022
# This program calculates the natural log of 2 using
# the alternating harmonic series up to the user's term


# Function that calculates the accuracy of the calculated sum to the
# true value of the natural log of 2.
def accuracy_perc(sum):
    NATLOG2 = 0.69314718056
    sum_accuracy = 100 - abs((NATLOG2 - sum) / NATLOG2 * 100)
    print(f"Value is ~{sum_accuracy}% accurate to the true value of ln2.\n")
    print(f"True value of ln(2) = {NATLOG2}")


def main():
    restart = ""

    while True:

        # Initializing variables

        sum = 0
        sign = -1

        # Asks the user for the decimal precision of the sum
        decimal_prec_str = input(
            "Enter the number of decimal places you want displayed: "
        )

        # Tries casting the decimal precision to an integer
        try:
            decimal_prec_int = int(decimal_prec_str)
        except:
            print("You must enter a positive whole number")
            input("Enter any key to restart: ")
            continue

        # Restarts if the decimal precision integer is less than 0
        if decimal_prec_int < 0:
            print("You must enter a positive whole number")
            input("Enter any key to restart: ")
            continue

        # Gets the number of terms to be calculated as a string
        terms_str = input("Enter the number of terms to be calculated: ")

        # Tries casting the term string to an integer
        try:
            terms_int = int(terms_str)
        except:
            print("You must enter a positive whole number")
            input("Enter any key to restart: ")
            continue

        # Restarts if the term integer is less than 0
        if terms_int <= 0:
            print("You must enter a positive term number")
            input("Enter any key to restart: ")
            continue

        # Prints the beginning of the equation
        print("ln(2) = ", end="")

        # Body code executed until counter is equal to the user's
        # term number
        for counter in range(1, terms_int + 1):
            # Used to determine if the term will be positive or negative
            sign *= -1

            # Calculates the sum
            fraction = 1 / counter
            sum += sign * fraction

            # Displays the alternating harmonic series. If statements are used
            # to determine the sign that needs to be displayed
            if counter == 1:
                print(f"{counter} ", end="")

            elif counter % 2 == 0:
                print(f"- 1/{counter} ", end="")

            else:
                print(f"+ 1/{counter} ", end="")

        sum_rounded = round(sum, decimal_prec_int)
        print()

        # Prints the sum of ln(2) to the user's specified precision
        print(f"ln(2) = {sum_rounded}")

        # Prints the accuracy of the sum to the true value of ln(2)
        accuracy_perc(sum)

        # Asks the user if they would like to restart
        restart = input("Enter 'q' to quit, enter anything else to restart: ")
        if restart == "q":
            break


if __name__ == "__main__":
    main()
