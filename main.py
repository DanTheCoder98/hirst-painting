import turtle

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("green4")

def draw_polygon(sides):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

draw_polygon(3)   # Triangle
draw_polygon(4)   # Square
draw_polygon(5)   # Pentagon
draw_polygon(6)   # Hexagon
draw_polygon(7)   # Heptagon
draw_polygon(8)   # Octagon
draw_polygon(9)   # Nonagon
draw_polygon(10)  # Decagon

screen = turtle.Screen()
screen.exitonclick()