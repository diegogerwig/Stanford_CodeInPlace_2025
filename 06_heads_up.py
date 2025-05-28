import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    lines = []
    with open(FILE_NAME) as f:
        for line in f:
            # removes whitespace characters (\n) from the start and end of the line
            line = line.strip() 
            # if the line was only whitespace characters, skip it 
            if line != "":
                lines.append(line)
                
    return lines


def main():
    # Milestone #1: Read the words from the file using the provided function
    words = get_words_from_file()
    
    print("Welcome to Heads Up!")
    print("Close your eyes when it's your turn, and have others describe the word without saying it!")
    print("Press Enter to see the next word, or type 'quit' to exit.\n")
    
    while True:
        # Wait for user input to continue or quit
        user_input = input("Press Enter for the next word (or 'quit' to exit): ")
        
        # Check if user wants to quit
        if user_input.lower() == 'quit':
            print("Thanks for playing Heads Up!")
            break
        
        # Milestone #2: Show a randomly chosen word from the list
        random_word = random.choice(words)
        
        print(f"\n*** {random_word.upper()} ***\n")
        
        # Milestone #3: Repeat - the loop continues to show another word


if __name__ == '__main__':
    main()