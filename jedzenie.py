import random
from turtle import Turtle


class Jedzenie(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        rand_x = random.randint(-180, 180)
        rand_y = random.randint(-180, 180)
        self.goto(rand_x, rand_y)
        self.reset()

    def reset(self):
        rand_x = random.randint(-180, 180)
        rand_y = random.randint(-180, 180)
        self.goto(rand_x, rand_y)
