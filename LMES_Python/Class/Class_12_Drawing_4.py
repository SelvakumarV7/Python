# Turtle only supports .GIF format.
# Ping-Pong Game:

import turtle

scr = turtle.Screen()
scr.title('Demo Game')
scr.bgcolor('Green')
scr.setup(800,800)

slide = turtle.Turtle()
slide.shape('square')
slide.shapesize(1,6)
slide.penup()
slide.goto(0,-350)

def slide_Left():
    x = slide.xcor()
    x-=30
    if x<-320:
        x=-320
    slide.setx(x)

def slide_Right():
    x = slide.xcor()
    x+=30
    if x>320:
        x = 320
    slide.setx(x)

scr.listen()
scr.onkeypress(slide_Left,'a')
scr.onkeypress(slide_Right, 'd')






turtle.done()
