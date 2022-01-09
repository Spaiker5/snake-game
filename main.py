import time
from turtle import Screen, Turtle
from snake import Snake
from jedzenie import Jedzenie
from tablica_wyników import Wynik

screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
jedzenie = Jedzenie()
tablica_wyników = Wynik()

screen.listen()

screen.onkey(snake.góra, "w")
screen.onkey(snake.dół, "s")
screen.onkey(snake.lewo, "a")
screen.onkey(snake.prawo, "d")

gramy = True

while gramy:
    screen.update()
    time.sleep(0.1)
    snake.ruch()

    if snake.łeb.distance(jedzenie) < 15:
        jedzenie.reset()
        tablica_wyników.zwiększanie_wyniku()
        snake.wydłóż()

    if snake.łeb.xcor() > 240 or snake.łeb.xcor() < -240 or snake.łeb.ycor() > 240 or snake.łeb.ycor() < -240:
        gramy = False
        tablica_wyników.game_over()
        tablica_wyników.reset()

    for segment in snake.segmenty[1:]:
        if snake.łeb.distance(segment) < 10:
            gramy = False
            tablica_wyników.game_over()
            tablica_wyników.reset()


screen.exitonclick()
