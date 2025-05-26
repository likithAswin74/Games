import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.go_up, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.car_move()
    # Detect collision with cars-
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()
    # Detect the successful crossing
    if player.ycor() > 280:
        player.go_to_start()
        cars.speed_up()
        scoreboard.level += 1
        scoreboard.increase_level()





screen.exitonclick()
