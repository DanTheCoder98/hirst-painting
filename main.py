import turtle
import random

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("green4")

screen = turtle.Screen()
screen.colormode(255)

def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor(r, g, b)
    
    draw_shape(shape_side_n)

screen.exitonclick()