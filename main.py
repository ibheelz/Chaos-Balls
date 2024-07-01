import turtle
import random

colors = ["red", "green", "blue", "white", "pink", "purple", "yellow", "grey", "brown", "cyan", "magneta"]

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

### Create a new ball ###

balls = []

ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.shapesize(0.5, 0.5)
ball.color(random.choice(colors))
ball.setheading(random.randint(0, 360))
balls.append(ball)

### Move ball ###
while True:
    for ball in balls:
        ball.forward(1)



screen.mainloop()
