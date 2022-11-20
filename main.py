import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross Road")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:

        if car.distance(player) < 40:
            game_is_on = False
            scoreboard.game_over()
    if player.finish():
        player.goto(0,-270)
        car_manager.level_up()
        scoreboard.next_level()

    if scoreboard.level == 5:
        scoreboard.finish_board()
        game_is_on = False






screen.exitonclick()