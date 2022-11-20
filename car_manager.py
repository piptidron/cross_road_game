from turtle import Turtle
import random

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.y_cars_position = (280, 240, 200, 160, 120, 80, 40, 0, -40, -80, -120, -160, -200)
        self.size_car = 0
        self.speed_car = 5


    def create_car(self):
        random_chance = random.randint(1,5)
        self.size_car = random_chance
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(2,2)
            new_car.penup()
            new_car.color("black")
            new_car.goto(250,random.choice(self.y_cars_position))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed_car)

    def level_up(self):
        self.speed_car += 10