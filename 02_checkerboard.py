from karel.stanfordkarel import *


def main():
    """
    Main program that coordinates Karel's actions to draw
    a pattern of beepers in the world.
    """
    put_beeper()
    # Karel draws one row and jumps to the next row until reaching the last row at the top
    while left_is_clear():
        draw_row()
        jump_row()
    # Drawing the last row at the top
    draw_row()
    # Karel returns to the starting point (bottom left corner)
    return_to_starting_point()



def draw_row():
    """
    Makes Karel draw a row by placing beepers
    every two steps whenever possible.
    """
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def jump_row():
    """
    After finishing drawing a row, Karel returns to the start
    and jumps to the next row.
    """
    turn_around()
    # Return to the beginning of the row
    while front_is_clear():
        move()

    # Determine if there's a beeper at the starting point
    if beepers_present():
        # If there's a beeper at the starting point of the first row,
        # Karel jumps to the next row, moves to the right, and places a beeper
        turn_right()
        move()
        turn_right()
        if front_is_clear():
            move()
            put_beeper()
    else:
        # If there's no beeper at the starting point,
        # Karel jumps to the next row and places a beeper
        turn_right()
        move()
        turn_right()
        put_beeper()


def return_to_starting_point():
    """
    Makes Karel return to the bottom left corner of the map.
    """
    turn_around()
    # Move completely downward
    while front_is_clear():
        move()
    turn_left()
    # Move completely to the left
    while front_is_clear():
        move()
    turn_left()


def turn_around():
    """
    Makes Karel turn 180 degrees.
    """
    turn_left()
    turn_left()


def turn_right():
    """
    Makes Karel turn right (90 degrees clockwise).
    """
    for _ in range(3):  # Using _ instead of i since we don't use the counter
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
