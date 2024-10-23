import turtle
import random

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("green4")
tim.width(10)
tim.speed(0)

screen = turtle.Screen()
screen.colormode(255)

direction = [0, 90, 180, 270]

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

def random_walk(lines):
    for _ in range(lines):
        tim.forward(20)
        tim.setheading(random.choice(direction))
        tim.pencolor(random_colour())

random_walk(200)

screen.exitonclick()