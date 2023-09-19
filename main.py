import turtle as t
import random

t.colormode(255)
screen = t.Screen()
Kaykay = t.Turtle()
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
              (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
              (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),
              (210, 200, 151)]

for b in range(1, 11):
    for i in range(10):
        Kaykay.penup()
        Kaykay.hideturtle()
        Kaykay.dot(20, random.choice(color_list))
        Kaykay.forward(50)

    Kaykay.home()
    Kaykay.setheading(90)
    Kaykay.forward(50 * b)
    Kaykay.setheading(0)

screen.exitonclick()
