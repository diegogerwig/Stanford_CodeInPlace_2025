from graphics import Canvas

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draw the red top half of the flag
    canvas.create_rectangle(
        0, 0,                # Top-left corner
        CANVAS_WIDTH, CANVAS_HEIGHT / 2,  # Bottom-right corner
        "red"               # Fill color
    )


if __name__ == '__main__':
    main()
