import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager(player)
score_board = Scoreboard(player)
screen.listen()
screen.onkey(player.up, "Up")

counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if not car_manager.get_collision_status():
        car_manager.move()

        if player.has_reached_finish():
            score_board.level_up()
            car_manager.update_speed()
            player.reset()
        if counter == 6:
            car_manager.build_car()
            counter = 0
        else:
            counter += 1
    else:
        score_board.game_over()




