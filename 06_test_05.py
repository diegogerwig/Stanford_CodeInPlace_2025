from graphics import Canvas

def main():
    # draws two cars
    canvas = Canvas(400, 400)
    x = 10
    y = 10
    draw_car(canvas, x, y)  # Changed: pass canvas, x, y as arguments

    x = 100
    y = 100
    draw_car(canvas, x, y)  # Changed: pass canvas, x, y as arguments

def draw_car(canvas, x, y):  # Changed: added parameters to receive canvas, x, y
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()
    