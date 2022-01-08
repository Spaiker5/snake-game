from jedzenie import Jedzenie
from turtle import Turtle

class Wynik(Turtle):

    def __init__(self):
        super().__init__()
        self.wynik = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.update_tablicy()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def update_tablicy(self):
        self.write(f"Wynik: {self.wynik}", align="center", font=("Arial", 24, "normal"))

    def zwiększanie_wyniku(self):
        self.wynik += 1
        self.clear()
        self.update_tablicy()