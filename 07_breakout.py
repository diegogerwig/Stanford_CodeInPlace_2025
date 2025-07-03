from graphics import Canvas
import time
import random
import math

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600
PADDLE_Y = CANVAS_HEIGHT - 30
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
BALL_RADIUS = 10

BRICK_GAP = 5
BRICK_WIDTH = (CANVAS_WIDTH - BRICK_GAP*9) / 10
BRICK_HEIGHT = 10

# Additional constants for the game
NUM_TURNS = 3
BRICK_ROWS = 10
BRICK_COLS = 10
BRICK_START_Y = 50
DELAY = 0.01

# Colors for brick rows (rainbow sequence)
BRICK_COLORS = ["red", "red", "orange", "orange", "yellow", "yellow", "green", "green", "cyan", "cyan"]


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Create the bricks
    bricks = create_bricks(canvas)
    
    # Create the paddle
    paddle = create_paddle(canvas)
    
    # Play the game for the specified number of turns
    for turn in range(NUM_TURNS):
        # Create a new ball for each turn
        ball = create_ball(canvas)
        
        # Set initial ball velocity (random angle downward)
        change_x, change_y = get_random_velocity()
        
        # Play one turn
        game_won = play_turn(canvas, ball, paddle, bricks, change_x, change_y)
        
        # Remove the ball after the turn ends
        canvas.delete(ball)
        
        if game_won:
            canvas.create_text(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, "YOU WIN!", "Arial", 30, "green")
            break
        elif turn == NUM_TURNS - 1:  # Last turn
            canvas.create_text(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, "GAME OVER", "Arial", 30, "red")
    
    # Keep the window open
    canvas.mainloop()


def create_bricks(canvas):
    """Create all the bricks and return them in a list"""
    bricks = []
    
    # Calculate starting x position to center the bricks
    total_brick_width = BRICK_COLS * BRICK_WIDTH + (BRICK_COLS - 1) * BRICK_GAP
    start_x = (CANVAS_WIDTH - total_brick_width) / 2
    
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            x = start_x + col * (BRICK_WIDTH + BRICK_GAP)
            y = BRICK_START_Y + row * (BRICK_HEIGHT + BRICK_GAP)
            
            # Get color for this row (every 2 rows same color)
            color = BRICK_COLORS[row]
            
            brick = canvas.create_rectangle(x, y, x + BRICK_WIDTH, y + BRICK_HEIGHT, color)
            bricks.append(brick)
    
    return bricks


def create_paddle(canvas):
    """Create the paddle"""
    x = (CANVAS_WIDTH - PADDLE_WIDTH) / 2
    y = PADDLE_Y
    return canvas.create_rectangle(x, y, x + PADDLE_WIDTH, y + PADDLE_HEIGHT, "black")


def create_ball(canvas):
    """Create the ball at the center of the screen"""
    x = CANVAS_WIDTH / 2 - BALL_RADIUS
    y = CANVAS_HEIGHT / 2 - BALL_RADIUS
    return canvas.create_oval(x, y, x + 2*BALL_RADIUS, y + 2*BALL_RADIUS, "black")


def get_random_velocity():
    """Get random initial velocity for the ball (heading downward)"""
    # Random angle between 45 and 135 degrees (downward)
    angle = random.uniform(math.pi/4, 3*math.pi/4)
    speed = 5
    change_x = speed * math.cos(angle)
    change_y = speed * math.sin(angle)
    return change_x, change_y


def play_turn(canvas, ball, paddle, bricks, change_x, change_y):
    """Play one turn of the game. Returns True if player wins, False if ball hits bottom"""
    bricks_remaining = len([b for b in bricks if b is not None])
    
    while True:
        # Move the ball
        canvas.move(ball, change_x, change_y)
        
        # Update paddle position based on mouse
        move_paddle(canvas, paddle)
        
        # Check for bounces off walls
        change_x, change_y = handle_wall_bounces(canvas, ball, change_x, change_y)
        
        # Check if ball hit the bottom (game over for this turn)
        ball_coords = canvas.coords(ball)
        
        # Handle different coordinate formats for bottom check
        if len(ball_coords) == 4:  # x1, y1, x2, y2
            ball_bottom = ball_coords[3]
        elif len(ball_coords) == 2:  # x, y (center coordinates)
            ball_bottom = ball_coords[1] + BALL_RADIUS
        else:
            ball_bottom = ball_coords[1] + BALL_RADIUS
            
        if ball_bottom >= CANVAS_HEIGHT:
            return False
        
        # Check for collisions with other objects
        collision_result = handle_collisions(canvas, ball, paddle, bricks, change_x, change_y)
        if collision_result:
            change_x, change_y, brick_hit = collision_result
            if brick_hit:
                bricks_remaining -= 1
                if bricks_remaining == 0:
                    return True  # Player wins!
        
        # Pause for animation
        time.sleep(DELAY)


def move_paddle(canvas, paddle):
    """Move the paddle to follow the mouse x-coordinate"""
    mouse_x = canvas.get_mouse_x()
    paddle_coords = canvas.coords(paddle)
    
    # Handle different coordinate formats
    if len(paddle_coords) == 4:  # x1, y1, x2, y2
        paddle_center_x = (paddle_coords[0] + paddle_coords[2]) / 2
        paddle_left = paddle_coords[0]
        paddle_right = paddle_coords[2]
    else:
        # Assume center coordinates
        paddle_center_x = paddle_coords[0]
        paddle_left = paddle_coords[0] - PADDLE_WIDTH / 2
        paddle_right = paddle_coords[0] + PADDLE_WIDTH / 2
    
    # Calculate how much to move the paddle
    move_x = mouse_x - paddle_center_x
    
    # Make sure paddle doesn't go off screen
    new_left = paddle_left + move_x
    new_right = paddle_right + move_x
    
    if new_left < 0:
        move_x = -paddle_left
    elif new_right > CANVAS_WIDTH:
        move_x = CANVAS_WIDTH - paddle_right
    
    canvas.move(paddle, move_x, 0)


def handle_wall_bounces(canvas, ball, change_x, change_y):
    """Handle bounces off the walls"""
    ball_coords = canvas.coords(ball)
    
    # Handle different coordinate formats
    if len(ball_coords) == 4:  # x1, y1, x2, y2
        ball_left = ball_coords[0]
        ball_right = ball_coords[2]
        ball_top = ball_coords[1]
    elif len(ball_coords) == 2:  # x, y (center coordinates)
        ball_left = ball_coords[0] - BALL_RADIUS
        ball_right = ball_coords[0] + BALL_RADIUS
        ball_top = ball_coords[1] - BALL_RADIUS
    else:
        # Fallback: assume first two are x, y coordinates
        ball_left = ball_coords[0] - BALL_RADIUS
        ball_right = ball_coords[0] + BALL_RADIUS
        ball_top = ball_coords[1] - BALL_RADIUS
    
    # Bounce off left or right walls
    if ball_left <= 0 or ball_right >= CANVAS_WIDTH:
        change_x = -change_x
    
    # Bounce off top wall
    if ball_top <= 0:
        change_y = -change_y
    
    return change_x, change_y


def handle_collisions(canvas, ball, paddle, bricks, change_x, change_y):
    """Handle collisions with paddle and bricks"""
    ball_coords = canvas.coords(ball)
    
    # Handle different coordinate formats for collision detection
    if len(ball_coords) == 4:  # x1, y1, x2, y2
        collision_coords = ball_coords
    elif len(ball_coords) == 2:  # x, y (center coordinates)
        x, y = ball_coords
        collision_coords = [x - BALL_RADIUS, y - BALL_RADIUS, x + BALL_RADIUS, y + BALL_RADIUS]
    else:
        # Fallback
        x, y = ball_coords[0], ball_coords[1]
        collision_coords = [x - BALL_RADIUS, y - BALL_RADIUS, x + BALL_RADIUS, y + BALL_RADIUS]
    
    # Get all objects that overlap with the ball
    colliding_objects = canvas.find_overlapping(
        collision_coords[0], collision_coords[1], 
        collision_coords[2], collision_coords[3]
    )
    
    # Check each colliding object
    for obj in colliding_objects:
        if obj == ball:
            continue  # Skip the ball itself
        
        if obj == paddle:
            # Ball hit paddle - bounce upward
            if change_y > 0:  # Only bounce if ball is moving downward
                change_y = -change_y
            return change_x, change_y, False
        
        # Check if it's a brick
        if obj in bricks:
            brick_index = bricks.index(obj)
            if bricks[brick_index] is not None:  # Brick still exists
                # Remove the brick
                canvas.delete(obj)
                bricks[brick_index] = None
                
                # Bounce the ball
                change_y = -change_y
                
                return change_x, change_y, True
    
    return None


if __name__ == '__main__':
    main()
