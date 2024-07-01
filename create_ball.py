from turtle import *
import random

colors = ["red", "green", "blue", "white", "pink", "purple", "yellow", "grey", "brown", "cyan", "magneta"]
balls = []

class new_ball:
  def __init__(self):
    
    self.ball = Turtle()
    self.ball.penup()
    self.ball.shape("circle")
    self.ball.shapesize(0.5, 0.5)
    self.ball.color(random.choice(colors))
    balls.append(self.ball)