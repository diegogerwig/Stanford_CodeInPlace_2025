def main():
    print("Enter a sequence of non-decreasing numbers.")
    
    # Get the first number
    first_num = float(input("Enter num: "))
    previous_num = first_num
    sequence_length = 1
    
    # Keep asking for numbers until we get a decreasing one
    while True:
        current_num = float(input("Enter num: "))
        
        # Check if current number is smaller than previous (decreasing)
        if current_num < previous_num:
            break
        
        # Number is non-decreasing, so continue
        sequence_length += 1
        previous_num = current_num
    
    print("Thanks for playing!")
    print(f"Sequence length: {sequence_length}")


if __name__ == "__main__":
    main()