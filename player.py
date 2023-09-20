from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go(self):
        self.fd(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        
