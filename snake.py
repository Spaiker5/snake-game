from turtle import Turtle

POZYCJE_STARTOWE = [(0, 0), (-20, 0), (-40, 0)]
DYS_RUCHU = 20
GÓRA = 90
DÓŁ = 270
LEWO = 180
PRAWO = 0


class Snake:

    def __init__(self):
        self.segmenty = []
        self.create_snake()
        self.łeb = self.segmenty[0]

    def create_snake(self):
        for pozycja in POZYCJE_STARTOWE:
            nowy_segment = Turtle("square")
            nowy_segment.penup()
            nowy_segment.color("white")
            nowy_segment.goto(pozycja)
            self.segmenty.append(nowy_segment)

    def ruch(self):
        for seg_num in range(len(self.segmenty) - 1, 0, -1):
            nowy_x = self.segmenty[seg_num - 1].xcor()
            nowy_y = self.segmenty[seg_num - 1].ycor()
            self.segmenty[seg_num].goto(nowy_x, nowy_y)
        self.łeb.forward(DYS_RUCHU)

    def góra(self):
        if self.łeb.heading() != DÓŁ:
            self.łeb.setheading(GÓRA)

    def dół(self):
        if self.łeb.heading() != GÓRA:
            self.łeb.setheading(DÓŁ)

    def lewo(self):
        if self.łeb.heading() != PRAWO:
            self.łeb.setheading(LEWO)

    def prawo(self):
        if self.łeb.heading() != LEWO:
            self.łeb.setheading(PRAWO)
