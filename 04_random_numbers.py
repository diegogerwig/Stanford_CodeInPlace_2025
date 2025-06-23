import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    """
    Prints 10 random numbers between 1 and 100, inclusive,
    with each number on a separate line.
    """
    for i in range(N_NUMBERS):
        # Generate a random number between MIN_VALUE and MAX_VALUE
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        
        # Print the random number on its own line
        print(random_number)


if __name__ == '__main__':
    main()