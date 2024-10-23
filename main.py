import turtle
import random

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("green4")
tim.width(10)
tim.speed(0)

screen = turtle.Screen()
screen.colormode(255)

direction = [90, 180, 270, 360]

def random_walk(lines):
    for _ in range(lines):
        tim.forward(20)
        tim.right(random.choice(direction))

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        tim.pencolor(r, g, b)

random_walk(200)

screen.exitonclick()