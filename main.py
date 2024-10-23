import turtle
import random

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("green4")
tim.speed("fastest")

screen = turtle.Screen()
screen.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

for _ in range(72):
    tim.circle(100)
    tim.left(5)

    tim.pencolor(random_colour())

screen.exitonclick()