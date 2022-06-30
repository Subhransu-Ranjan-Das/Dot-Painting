from painting import color_list
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.hideturtle()
screen.colormode(255)
tim.penup()


def set_pos():
    tim.speed("fastest")
    tim.penup()
    tim.setx(-225)
    tim.sety(-225)
    tim.pendown()


def color(color_list):
    tup = random.choice(color_list)
    print(tup)
    return tup


def move(color_list):
    for n in range(10):
        tim.speed("fastest")
        x = color(color_list)
        tim.dot(15, x)
        tim.penup()
        tim.forward(50)
        tim.pendown()
        print(n)


def move_up():
    k = 0
    for n in range(9):
        k += 50
        tim.penup()
        tim.sety(-225 + k)
        tim.setx(-225)
        move(color_list)


set_pos()
move(color_list)
move_up()
screen.exitonclick()
