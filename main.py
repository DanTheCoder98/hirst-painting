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
tim.color("green4")
tim.shape("turtle")

screen.exitonclick()