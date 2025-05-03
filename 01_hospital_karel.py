from karel.stanfordkarel import *


def main():
    """
    Karel builds hospitals at locations marked with beepers.
    Each hospital is a 2×3 structure (2 columns, 3 rows tall).
    """
    # Handle the case when Karel starts on a beeper
    if beepers_present():
        build_hospital()

    # Move and check for beepers until reaching the wall
    while front_is_clear():
        move()
        if beepers_present():
            build_hospital()


def build_hospital():
    """
    Builds a hospital at Karel's current position.
    A hospital is a 2×3 structure (2 columns, 3 rows tall).
    
    Precondition: Karel is standing on a beeper
    Postcondition: Karel is at the bottom of the second column facing east
    """
    # Remove the supply beeper
    pick_beeper()

    # Build the first column
    turn_left()  # Face north
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

    # Move to position for second column
    turn_right()  # Face east
    move()
    turn_right()  # Face south

    # Build the second column (going down)
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

    # Return to the first row and face east
    turn_left()  # Face east


def turn_right():
    """
    Makes Karel turn right by turning left three times.
    """
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()
