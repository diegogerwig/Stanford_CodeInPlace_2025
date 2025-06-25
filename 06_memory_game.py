import random

NUM_PAIRS = 3

def clear_terminal():
    for _ in range(20):
        print()


def get_valid_index(displayed, prompt, other_index=None):
    while True:
        index_str = input(prompt)
        if not index_str.isdigit():
            print("Not a number. Try again.")
            continue
        index = int(index_str)
        if index < 0 or index >= len(displayed):
            print("Invalid index. Try again.")
            continue
        if displayed[index] != '*':
            print("This number has already been matched. Try again.")
            continue
        if other_index is not None and index == other_index:
            print("You entered the same index twice. Try again.")
            continue
        return index

def main():
    # Milestone 1: Create the truth list
    truth = []
    for i in range(NUM_PAIRS):
        truth.extend([i, i])
    
    # Milestone 2: Shuffle the truth list
    random.shuffle(truth)

    # Milestone 3: Create a displayed list
    displayed = ['*'] * len(truth)

    # Milestone 6: Play until all pairs matched
    while '*' in displayed:
        print(displayed)
        idx1 = get_valid_index(displayed, "Enter an index: ")
        idx2 = get_valid_index(displayed, "Enter an index: ", other_index=idx1)

        if truth[idx1] == truth[idx2]:
            displayed[idx1] = truth[idx1]
            displayed[idx2] = truth[idx2]
            print("Match!")
            clear_terminal()
        else:
            print(f"Value at index {idx1} is {truth[idx1]}")
            print(f"Value at index {idx2} is {truth[idx2]}")
            print("No match. Try again.")
            input("Press Enter to continue...")
            clear_terminal()

    print(displayed)
    print("Congratulations! You won!")

if __name__ == '__main__':
    main()
