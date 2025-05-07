import random

def main():
    # Set up the game
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate the secret number
    secret_number = random.randint(1, 100)
    
    # Initialize variables
    guess_count = 0
    max_guesses = 7
    has_won = False
    
    # Main game loop
    while guess_count < max_guesses and not has_won:
        # Calculate remaining guesses
        guesses_left = max_guesses - guess_count
        print(f"You have {guesses_left} guesses left.")
        
        # Get user's guess
        user_input = input("Enter your guess: ")
        
        # Validate input is a number
        try:
            guess = int(user_input)
        except ValueError:
            print("That's not a valid number! Try again.")
            continue
        
        # Count this attempt
        guess_count += 1
        
        # Check the guess
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            has_won = True
            print(f"Congratulations! You guessed the number in {guess_count} tries!")
    
    # If the player ran out of guesses
    if not has_won:
        print(f"Game over! The number was {secret_number}.")
        print("Better luck next time!")

if __name__ == "__main__":
    main()