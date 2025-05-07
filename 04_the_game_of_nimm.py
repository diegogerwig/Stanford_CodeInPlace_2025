
def main():
    """
    Implementation of the Ancient Game of Nimm where:
    - The game starts with 20 stones
    - Players alternate turns taking 1 or 2 stones
    - The last player to take a stone loses
    """
    
    # Start with 20 stones
    stones = 20
    
    # Track whose turn it is (1 or 2)
    current_player = 1
    
    # Continue until no stones remain
    while stones > 0:
        # Display current game state
        print(f"There are {stones} stones left.")
        
        # Prompt current player
        stones_to_remove = int(input(f"Player {current_player} would you like to remove 1 or 2 stones? "))
        
        # Validate input - must be 1 or 2
        while stones_to_remove != 1 and stones_to_remove != 2:
            stones_to_remove = int(input("Please enter 1 or 2: "))
        
        # If only 1 stone remains, player can only take 1
        if stones == 1 and stones_to_remove > 1:
            stones_to_remove = 1
        
        # Remove stones
        stones -= stones_to_remove
        
        # Print empty line for readability
        print()
        
        # If no stones remain, current player took the last stone and loses
        if stones == 0:
            # The other player wins
            winner = 2 if current_player == 1 else 1
            print(f"Player {winner} wins!")
        else:
            # Switch to other player's turn
            current_player = 2 if current_player == 1 else 1


if __name__ == '__main__':
    main()




