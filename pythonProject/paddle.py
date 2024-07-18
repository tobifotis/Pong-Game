from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

        self.penup()
        self.setpos((x, y))

    def go_up(self):
        new_y = self.ycor() + 20

        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -250:
            self.goto(self.xcor(), new_y)
