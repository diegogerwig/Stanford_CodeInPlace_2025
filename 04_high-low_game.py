import random

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0

    for round_num in range(1, 6):
        print(f"Round {round_num}")  
        
        user_number = random.randint(1, 100)
        print(f"Your number is {user_number}")
        
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        computer_number = random.randint(1, 100)

        if (guess == "higher" and user_number > computer_number) or \
           (guess == "lower" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}")
        print()  

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
