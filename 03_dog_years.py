# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18


def main():
    # Ask the user to input an age in calendar years
    calendar_years = float(input("Enter an age in calendar years: "))

    # Calculate dog years by multiplying calendar years by the dog years multiplier
    dog_years = calendar_years * DOG_YEARS_MULTIPLIER

    # Display the result
    print(f"That's {dog_years} in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()

