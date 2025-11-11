from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 250)
        self.write(f"Score: {self.score}", align="center", font=("Verdana",36, "normal"))
    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Verdana", 36, "normal"))
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Verdana", 36, "normal"))