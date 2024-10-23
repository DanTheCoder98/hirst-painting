import turtle

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("green4")

def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)

screen = turtle.Screen()
screen.exitonclick()