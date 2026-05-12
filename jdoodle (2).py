#Made by Gabriel Morales 05/12/2026
#This code allows for the user to learn the times table from 10-20

import random

def main():
    print("Welcome to the Times Table Learning Game!")
    print("This program will show you the multiplication table from 10 to 20")
    print("using your chosen number.\n")
    
    # Ask the user for a positive integer with input validation
    while True:
        try:
            user_number = int(input("Please enter a positive integer: "))
            if user_number > 0:
                break
            else:
                print("Please enter a positive integer (greater than 0).")
        except ValueError:
            print("Please enter a valid integer.")
    
    # Use a while loop to print the multiplication times table from 10 to 20
    print(f"\nMultiplication table for {user_number} (from 10 to 20):")
    print("-" * 30)
    
    # Initialize counter
    multiplier = 10
    
    # While loop to generate and print the times table
    while multiplier <= 20:
        result = user_number * multiplier
        print(f"{user_number} x {multiplier} = {result}")
        multiplier += 1
    
    print("-" * 30)
    print("Thank you for using the Times Table Learning Game!")

# Call the main function
if __name__ == "__main__":
    main()
