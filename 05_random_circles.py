from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draw N_CIRCLES random circles on the canvas
    for i in range(N_CIRCLES):
        draw_random_circle(canvas)

def draw_random_circle(canvas):
    """
    Draws a single random circle on the canvas with a random position
    and a random color.
    """
    # Generate random x and y coordinates for the circle
    x = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
    y = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)
    
    # Get a random color for the circle
    color = random_color()
    
    # Draw the circle at the random position with the random color
    canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE, color)
    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()