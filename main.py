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

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(40)

screen.exitonclick()