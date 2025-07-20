# Traffic Signal:

import turtle

scr = turtle.Screen()
scr.title('Traffic Signal')
scr.setup(500,700)

rhombus = turtle.Turtle()
rhombus.fillcolor('yellow')
rhombus.begin_fill()
rhombus.pensize(8)
rhombus.penup()
rhombus.goto(0,-200)
rhombus.pendown()

for i in range(4):
    rhombus.lt(45)
    rhombus.fd(300)
    rhombus.lt(45)

rhombus.end_fill()
rhombus.hideturtle()

box = turtle.Turtle()
box.pensize(5)
box.fillcolor('black')
box.begin_fill()
box.penup()
box.goto(-30,-90)
box.pendown()

for i in range(2):
    box.fd(70)
    box.lt(90)
    box.fd(200)
    box.lt(90)
box.end_fill()
box.hideturtle()

red = turtle.Turtle()
red.pensize(1)
red.pencolor('white')
red.fillcolor('red')
red.begin_fill()
red.penup()
red.goto(5,60)
red.pendown()
red.circle(20)
red.end_fill()
red.hideturtle()

yellow = turtle.Turtle()
yellow.pensize(1)
yellow.pencolor('white')
yellow.fillcolor('yellow')
yellow.begin_fill()
yellow.penup()
yellow.goto(5,-10)
yellow.pendown()
yellow.circle(20)
yellow.end_fill()
yellow.hideturtle()

green = turtle.Turtle()
green.pensize(1)
green.pencolor('white')
green.fillcolor('green')
green.begin_fill()
green.penup()
green.goto(5,-80)
green.pendown()
green.circle(20)
green.end_fill()
green.hideturtle()





turtle.done()
