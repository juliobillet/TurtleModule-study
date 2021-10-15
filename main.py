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

# directions = [0, 90, 180, 270]
#
# for step in range(201):
#     josefina.forward(30)
#     random_color = random(), random(), random()
#     josefina.pencolor(random_color)
#     josefina.setheading(choice(directions))

# for edges_number in range(3, 11):
#    random_color = random(), random(), random()
#    josefina.pencolor(random_color)
#
#    for edge in range(edges_number):
#        josefina.forward(100)
#        josefina.right(360 / edges_number)
