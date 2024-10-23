import turtle

timmy_the_turtle = turtle.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green4")

def line():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)


for n in range(0, 4):
    line()

screen = turtle.Screen()
screen.exitonclick()
