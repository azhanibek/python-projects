from turtle import Screen, Turtle
import time
import snake
import food
import scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
scoreboard = scoreboard.ScoreBoard()
snake = snake.Snake()
food = food.Food()
screen.listen()
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.create_new()
        scoreboard.add_score()
        snake.grow()
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        scoreboard.game_over()
    for snake_part in snake.snake_body[1:]:
        if snake.head.distance(snake_part) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()