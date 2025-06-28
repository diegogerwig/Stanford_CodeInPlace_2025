MAX_VALUE = 17

def main():
    for i in range(1, MAX_VALUE + 1):
        to_say = fizzbuzz(i)
        print(to_say)

def fizzbuzz(n):
    """
    Takes in a positive integer (n) and returns
    what the player should say at that value.
    """
    if n % 3 == 0 and n % 5 == 0:
        return "Fizzbuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

if __name__ == '__main__':
    main()
