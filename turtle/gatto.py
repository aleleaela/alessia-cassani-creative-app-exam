import turtle
from PIL import Image

def draw_pixel(color, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def image_to_pixel_art(image_path, pixel_size=10):
    image = Image.open(image_path)
    image = image.resize((70, 70))
    image = image.convert('RGB')

    turtle.speed(0.5)
    turtle.hideturtle()
    turtle.tracer(1)

    width, height = image.size
    start_x = -width * pixel_size // 2
    start_y = height * pixel_size // 2

    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            color = (r / 255, g / 255, b / 255)
            draw_pixel(color, start_x + x * pixel_size, start_y - y * pixel_size, pixel_size)

    turtle.update()
    turtle.done()

image_path = 'image/IMG_9601.jpg'
image_to_pixel_art(image_path)
