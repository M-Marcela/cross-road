from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-200, y=250)
        self.update_text()

    def update_text(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align="center", font=FONT)
        

    def next_level(self):
        self.level += 1
        self.clear()
        self.update_text()
        
