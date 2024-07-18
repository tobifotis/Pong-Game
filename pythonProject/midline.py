from turtle import Turtle


class Midline(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(0, -400)
        self.setheading(90)
        self.pendown()
        for _ in range(50):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
