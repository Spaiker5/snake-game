from turtle import Turtle

POZYCJE_STARTOWE = [(0, 0), (-20, 0), (-40, 0)]
DYS_RUCHU = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segmenty = []
        self.create_snake()
        self.head = self.segmenty[0]

    def create_snake(self):
        for pozycja in POZYCJE_STARTOWE:
            self.dodaj_segment(pozycja)

    def dodaj_segment(self, pozycja):
        nowy_segment = Turtle("square")
        nowy_segment.penup()
        nowy_segment.color("white")
        nowy_segment.goto(pozycja)
        self.segmenty.append(nowy_segment)

    def add_segment(self):
        self.dodaj_segment(self.segmenty[-1].position())

    def ruch(self):
        for seg_num in range(len(self.segmenty) - 1, 0, -1):
            nowy_x = self.segmenty[seg_num - 1].xcor()
            nowy_y = self.segmenty[seg_num - 1].ycor()
            self.segmenty[seg_num].goto(nowy_x, nowy_y)
        self.head.forward(DYS_RUCHU)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
