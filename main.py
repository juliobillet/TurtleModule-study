from turtle import Turtle, Screen, mode
from random import *

mode("logo")

josefina = Turtle()
josefina.shape("turtle")
josefina.color("DeepSkyBlue")
josefina.speed(0)

for i in range(0, 360, 10):
    random_color = random(), random(), random()
    josefina.pencolor(random_color)
    josefina.circle(100)
    josefina.setheading(-i)
    josefina.circle(100)


screen = Screen()
screen.exitonclick()
