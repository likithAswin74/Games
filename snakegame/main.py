from turtle import Screen
from snake import Snake
from egg import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()

food = Food()
score = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

move = True
while move:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.increase_score()


    # DETECT COLLISION WITH WALL
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.restart()
        snake.reset_snake()
        # move = False


    # DETECT COLLISION WITH BODY
    for segments in snake.segments[2:]:
        if snake.head.distance(segments) < 10:
            score.restart()
            snake.reset_snake()
            # move = False


screen.exitonclick()
# if score.score > score.high_score:
#score.high_score = score.score
