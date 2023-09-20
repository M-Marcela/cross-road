import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.generate_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    if player.is_at_finish_line():
        scoreboard.next_level()
        car_manager.speed_up()



