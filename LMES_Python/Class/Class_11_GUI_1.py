# GUI - Graphical User Interface.

# Turtle:

import turtle

scr = turtle.Screen()
scr.title('First drawing')
scr.bgcolor()
scr.setup(900,900)

pen = turtle.Turtle()
pen.shape('turtle')
pen.pensize(5)
pen.speed(5)
pen.fillcolor('Red')
pen.begin_fill()
pen.circle(150)
pen.end_fill()

pen.fillcolor('Blue')
pen.begin_fill()
for i in range(4):
    pen.fd(200)
    pen.rt(90)
pen.end_fill()
pen.hideturtle()
turtle.done()