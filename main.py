import turtle
import random
import math

colors = ["red", "green", "blue", "pink", "purple", "yellow", "grey", "brown", "cyan"]

### Create Turtle Screen ###

screen = turtle.Screen()
screen.title("C H A O S    B A L L")
screen.bgcolor("black")

### Create Circle Container ###

container = turtle.Turtle()
container.hideturtle()
container.speed(100)
container.color("white")
container.pensize(3)
container.penup()
container.goto(0, -300)
container.pendown()
container.circle(300)

### Create a new ball ###

balls = []

def create_ball():
    ball = turtle.Turtle()
    ball.penup()
    ball.shape("circle")
    ball.shapesize(0.5, 0.5)
    ball.color(random.choice(colors))
    ball.setheading(random.randint(0, 360))
    balls.append(ball)

create_ball()

### Move ball ###

while True:
    for ball in balls:
        ball.forward(1)
        x, y = ball.position()
        distance_from_center = math.sqrt(x**2 + y**2)
        if distance_from_center >= 295:
            create_ball()
            ball.setheading(-(random.randint(0, 360)))
            ball.forward(1)




screen.mainloop()
