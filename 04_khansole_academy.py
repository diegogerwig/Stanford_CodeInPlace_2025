import random

def main():
    print("Khansole Academy")
    
    # Generate two random 2-digit integers (between 10 and 99)
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    
    # Calculate the correct answer
    correct_answer = num1 + num2
    
    # Present the problem to the user
    print(f"What is {num1} + {num2}?")
    
    # Get the user's answer
    user_answer = int(input("Your answer: "))
    
    # Check if the answer is correct
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect.")
        print(f"The expected answer is {correct_answer}")
    
if __name__ == '__main__':
    main()