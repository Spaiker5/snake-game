import time
from turtle import Screen

from jedzenie import Jedzenie
from snake import Snake
from tablica import Wynik

screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
jedzenie = Jedzenie()
tablica = Wynik()

screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

gramy = True

while gramy:
    screen.update()
    time.sleep(0.1)
    snake.ruch()

    if snake.head.distance(jedzenie) < 15:
        jedzenie.reset()
        tablica.wynik_up()
        snake.add_segment()

    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        gramy = False
        tablica.game_over()
        tablica.reset()

    for segment in snake.segmenty[1:]:
        if snake.head.distance(segment) < 10:
            gramy = False
            tablica.game_over()
            tablica.reset()

screen.exitonclick()
