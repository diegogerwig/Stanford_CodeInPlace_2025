import random


def main():
    # Ask user for number of sides on the dice
    sides = int(input("How many sides does your dice have? "))

    # Simulate the dice roll
    roll = random.randint(1, sides)

    # Print the result
    print("Your roll is", roll)


if __name__ == '__main__':
    main()


