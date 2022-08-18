import random
from turtle import Turtle
from random import Random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self, player):
        self.cars = []
        # for i in -230:230:40
        self.player = player
        self.car_speed = STARTING_MOVE_DISTANCE

    def build_car(self):
        car = Turtle()
        car.shape("square")
        car.penup()
        car.goto(300, random.randint(-230, 230))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.setx(car.xcor() - self.car_speed)

    def get_collision_status(self):
        for car in self.cars:
            if car.distance(self.player) < 20 or self.player.ycor() + 10 == car.ycor():
                #print(f"Collision with {car.color()}!")
                return True

    def update_speed(self):
        self.car_speed += MOVE_INCREMENT




