"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""


def main():
    n = int(input("Enter a number:"))
    while True:
        if n % 2 == 0:
            next_n = n // 2
            print(f"{n} is even, so I take half: {next_n}")
        else:
            next_n = 3 * n + 1
            print(f"{n} is odd, so I make 3n+1: {next_n}")
        if next_n == 1:
            break
        n = next_n


if __name__ == "__main__":
    main()
