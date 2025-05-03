"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""


def main():
    print("This program multiplies two numbers.")
    # Get the first number from the user
    num1 = input("Enter first number: ")
    # Convert the first input to an integer
    num1 = int(num1)

    # Get the second number from the user
    num2 = input("Enter second number: ")
    # Convert the second input to an integer
    num2 = int(num2)

    # Calculate the product of the two numbers
    product = num1 * num2

    # Print the result
    print(product)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
