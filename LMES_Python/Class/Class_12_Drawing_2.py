# Crackers:

import turtle
import random

scr = turtle.Screen()
scr.title('Crackers')
scr.bgcolor('black')
scr.setup(500,500)

crackers = turtle.Turtle()
crackers.color('gold')
crackers.speed(100)

for i in range(15):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    crackers.penup()
    crackers.goto(x,y)
    crackers.pendown()
    colors = ['red', 'Blue', 'Silver', 'yellow', 'pink', 'Green', 'brown', 'orange']
    c = random.choice(colors)
    crackers.color(c)
    s = random.randint(30,50)
    for i in range(36):
        crackers.fd(s)
        crackers.bk(s)
        crackers.rt(10)
crackers.hideturtle()
turtle.done()