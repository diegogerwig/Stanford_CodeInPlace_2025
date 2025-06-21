from karel.stanfordkarel import *


def main():
    """
    Main program that places beepers at both ends of the world,
    fills the line with beepers at every other position,
    and then cleans up all beepers before stopping at the first beeper.
    """
    # Place beepers at both ends
    place_end_beepers()

    # Fill the line with beepers at alternate positions
    fill_alternate_positions()

    # Clean up all beepers
    collect_all_beepers()

    # Move to final position
    find_first_beeper()



def place_end_beepers():
    """Place beepers at both ends of the world."""
    put_beeper()  # Place beeper at starting position

    # Move to opposite end
    while front_is_clear():
        move()

    put_beeper()  # Place beeper at ending position
    turn_around()
    move()


def fill_alternate_positions():
    """Fill the line with beepers at every other position."""
    while no_beepers_present():
        # Move until finding a beeper
        while no_beepers_present():
            move()

        # Place a beeper between this and the previous beeper
        turn_around()
        move()
        put_beeper()
        move()

    # Final adjustments based on direction
    if facing_west():
        put_beeper()
    else:
        turn_around()
        move()
        put_beeper()


def collect_all_beepers():
    """Pick up all beepers on the line."""
    # Move to the end of the world
    while front_is_clear():
        move()

    turn_around()

    # Pick up all beepers while moving back
    while front_is_clear():
        pick_beeper()
        move()

    pick_beeper()  # Pick up the last beeper


def find_first_beeper():
    """Move until finding a beeper, then turn around."""
    turn_around()
    while no_beepers_present():
        move()
    turn_around()


def turn_around():
    """Turn Karel around 180 degrees."""
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()
