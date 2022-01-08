import time
from turtle import Screen, Turtle
from snake import Snake
from jedzenie import Jedzenie
screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
jedzenie = Jedzenie()
screen.listen()

screen.onkey(snake.góra, "w")
screen.onkey(snake.dół, "s")
screen.onkey(snake.lewo, "a")
screen.onkey(snake.prawo, "d")

gramy = True

while gramy:
    screen.update()
    time.sleep(0.3)
    snake.ruch()

    if snake.łeb.distance(jedzenie) < 15:
        jedzenie.reset()

screen.exitonclick()
