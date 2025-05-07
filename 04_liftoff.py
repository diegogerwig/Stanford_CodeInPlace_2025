"""
Program: Liftoff
--------------------
Countdown from 10 to 1 and then print Liftoff!
"""

def main():
    # Print each number in the countdown on its own line
    for i in range(10):
        # Calculate the countdown number (10 minus the loop iteration)
        countdown_number = 10 - i
        # Print with a newline after each number
        print(countdown_number)
    
    # Print Liftoff! after the countdown is complete
    print("Liftoff!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()