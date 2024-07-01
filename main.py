import turtle
from create_ball import new_ball

### Create Turtle Screen ###

screen = turtle.Screen()
screen.title("C H A O S    B A L L")
screen.bgcolor("black")

### Create Circle Container ###

o = turtle.Turtle()
o.hideturtle()
o.speed(100)
o.color("white")
o.pensize(3)
o.penup()
o.goto(0, -300)
o.pendown()
o.circle(300)

new_ball()

screen.mainloop()