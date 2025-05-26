from karel.stanfordkarel import *

def main():
    move()
    
    # Create 4 waves
    make_wave()
    move_to_next_wave_position()
    
    make_wave()
    move_to_next_wave_position()
    
    make_wave()
    move_to_next_wave_position()
    
    make_wave()

def make_wave():
    """Create a single wave (triangle of 3 beepers)"""
    # Put beeper at bottom of wave
    put_beeper()
    
    # Go up and put middle beeper
    turn_left()
    move()
    put_beeper()
    
    # Go up and put top beeper
    move()
    put_beeper()
    
    # Go back down to bottom row
    turn_around()
    move()
    move()
    turn_left()

def move_to_next_wave_position():
    """Move to the starting position of the next wave"""
    move()  # Skip one column (gap)
    move()  # Move to next wave column

def turn_around():
    """Turn Karel around 180 degrees"""
    turn_left()
    turn_left()

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()