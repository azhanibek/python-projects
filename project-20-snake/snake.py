from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake_body = []
        for i in range(0, 3):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.setpos(x=i * (-20), y=0)
            self.snake_body.append(new_turtle)
        self.head = self.snake_body[0]
    def move(self):
        for snake_part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_part - 1].xcor()
            new_y = self.snake_body[snake_part - 1].ycor()
            self.snake_body[snake_part].goto(new_x, new_y)
        self.head.forward(20)
    def left(self):
        self.head.left(90)
    def right(self):
        self.head.right(90)
    def grow(self):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        last_turtle = self.snake_body[len(self.snake_body) - 1]
        new_turtle.setpos(last_turtle.xcor(), last_turtle.ycor())
        self.snake_body.append(new_turtle)