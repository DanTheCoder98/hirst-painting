import turtle

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("green4")

for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen = turtle.Screen()
screen.exitonclick()
