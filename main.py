import colorgram
import turtle
import random

colours = colorgram.extract("image.jpg", 50)

colour_palette = []

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b

    colour_palette.append((r, g, b))

turtle.colormode(255)
screen = turtle.Screen()
screen.title("Hirst Painting")
screen.bgcolor("white")

tim = turtle.Turtle()
tim.hideturtle()

def draw_dot(x, y):
    tim.penup()
    tim.goto(x, y)
    tim.pendown()
    tim.dot(20, random.choice(colour_palette))

start_x = -200
start_y = -200

for row in range(10):
    for col in range(10):
        draw_dot(start_x + col * 50, start_y + row * 50)

screen.exitonclick()