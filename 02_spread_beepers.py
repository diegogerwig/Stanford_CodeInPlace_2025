from karel.stanfordkarel import *

"""
Beeper Distribution Program

This program handles a scenario where Karel needs to distribute beepers.
Each row starts with a stack of beepers. Karel must pick them up one by one
and spread them down the row. The challenge is that Karel can't count and
starts with infinite beepers, so we need to be careful about the algorithm.
"""


def main():
    """
    Main program execution: Karel moves forward once, spreads the beepers,
    and then steps back to the original position.
    """
    move()
    spread()
    step_back()


def spread():
    """
    Spreads beepers from a stack along a row.
    
    Process:
    1. While beepers exist at the current position, pick one up
    2. If more beepers remain, move to the end of the current placement
    3. Place the picked-up beeper
    4. Reset position back to the stack
    5. Place one final beeper when the stack is empty
    """
    while beepers_present():
        pick_beeper()
        if beepers_present():
            move_to_end()
            put_beeper()
            reset()
    put_beeper()


def move_to_end():
    """
    Moves Karel to the end of the current beeper placement.
    Karel stops when reaching a position without beepers.
    """
    while beepers_present():
        move()


def reset():
    """
    Resets Karel's position back to the stack of beepers.
    Karel turns around, moves to the wall, turns around again,
    and moves forward one space to position at the stack.
    """
    turn_around()
    move_to_wall()
    turn_around()
    move()


def move_to_wall():
    """
    Moves Karel forward until reaching a wall.
    """
    while front_is_clear():
        move()


def turn_around():
    """
    Makes Karel turn around (180 degrees) by turning left twice.
    """
    turn_left()
    turn_left()


def step_back():
    """
    Makes Karel step back one position and face the original direction.
    """
    turn_around()
    move()
    turn_around()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
