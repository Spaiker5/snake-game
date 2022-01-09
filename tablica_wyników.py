from jedzenie import Jedzenie
from turtle import Turtle


class Wynik(Turtle):

    def __init__(self):
        super().__init__()
        self.wynik = 0
        with open("data.txt") as data:
            self.hscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.update_tablicy()


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def update_tablicy(self):
        self.goto(0, 200)
        self.write(f"Wynik: {self.wynik}  Highscore: {self.hscore}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.wynik > self.hscore:
            self.hscore = self.wynik
            with open("data.txt", mode="w") as data:
                data.write(f"{self.wynik}")
        self.update_tablicy()
        self.wynik = 0

    def zwiększanie_wyniku(self):
        self.wynik += 1
        self.clear()
        self.update_tablicy()
