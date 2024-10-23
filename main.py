import turtle

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("green4")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = turtle.Screen()
screen.exitonclick()
