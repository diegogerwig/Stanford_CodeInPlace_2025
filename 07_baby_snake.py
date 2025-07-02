from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Milestone #1: Set up the World
    # Create player (blue square) at top left corner
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, 'blue')
    
    # Create goal (red square) at a random position that's a multiple of 20
    goal_x = 360  # Starting position as suggested
    goal_y = 360
    goal = canvas.create_rectangle(goal_x, goal_y, goal_x + SIZE, goal_y + SIZE, 'red')
    
    # Milestone #2: Animation setup
    # Player starts traveling to the right
    direction = 'right'
    
    # Animation loop
    while True:
        # Milestone #3: Handle Key Press
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            direction = 'left'
        elif key == 'ArrowRight':
            direction = 'right'
        elif key == 'ArrowUp':
            direction = 'up'
        elif key == 'ArrowDown':
            direction = 'down'
        
        # Move player based on current direction
        if direction == 'right':
            canvas.move(player, SIZE, 0)
        elif direction == 'left':
            canvas.move(player, -SIZE, 0)
        elif direction == 'up':
            canvas.move(player, 0, -SIZE)
        elif direction == 'down':
            canvas.move(player, 0, SIZE)
        
        # Milestone #4: Detecting collisions (out of bounds)
        player_x = canvas.get_left_x(player)
        player_y = canvas.get_top_y(player)
        
        # Check if player is out of bounds
        if (player_x < 0 or player_x >= CANVAS_WIDTH or 
            player_y < 0 or player_y >= CANVAS_HEIGHT):
            print("Game Over! Player went out of bounds.")
            break
        
        # Milestone #5: Moving the goal
        # Check if player hits the goal
        goal_x = canvas.get_left_x(goal)
        goal_y = canvas.get_top_y(goal)
        
        if player_x == goal_x and player_y == goal_y:
            print("Goal reached! Moving goal to new location.")
            
            # Generate new random position for goal (multiple of 20)
            new_goal_x = random.randint(0, (CANVAS_WIDTH - SIZE) // SIZE) * SIZE
            new_goal_y = random.randint(0, (CANVAS_HEIGHT - SIZE) // SIZE) * SIZE
            
            # Move goal to new position
            canvas.moveto(goal, new_goal_x, new_goal_y)
        
        # Sleep to control animation speed
        time.sleep(DELAY)

if __name__ == '__main__':
    main()