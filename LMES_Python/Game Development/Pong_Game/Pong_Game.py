# Pong Game:

import turtle
scr = turtle.Screen()
scr.bgpic('screen.png')

scr.addshape('right.gif')
scr.addshape('left.gif')
scr.addshape('ball.gif')

player_right = turtle.Turtle()
player_right.shape('right.gif')
player_right.penup()
player_right.goto(350,-140)

player_left = turtle.Turtle()
player_left.shape('left.gif')
player_left.penup()
player_left.goto(-350,150)

ball = turtle.Turtle()
ball.shape('ball.gif')
ball.penup()

leftpen = turtle.Turtle()
leftpen.penup()
leftpen.hideturtle()
leftpen.goto(-400,250)
leftpen.color('white')
leftpen.write('Leftplayer Score = 0',font = ('Courier',20,'bold'))

rightpen = turtle.Turtle()
rightpen.penup()
rightpen.hideturtle()
rightpen.goto(100,250)
rightpen.color('white')
rightpen.write('Rightplayer Score = 0',font = ('Courier',20,'bold'))

def left_up():
    y = player_left.ycor()
    player_left.sety(y+10)

def left_down():
    y = player_left.ycor()
    player_left.sety(y-10)

def left_right():
    x = player_left.xcor()
    player_left.setx(x+10)

def left_left():
    x = player_left.xcor()
    player_left.setx(x-10)

def right_up():
    y = player_right.ycor()
    player_right.sety(y+10)

def right_down():
    y = player_right.ycor()
    player_right.sety(y-10)

def right_right():
    x = player_right.xcor()
    player_right.setx(x+10)

def right_left():
    x = player_right.xcor()
    player_right.setx(x-10)



scr.listen()
scr.onkeypress(left_up,'w')
scr.onkeypress(left_down,'s')
scr.onkeypress(left_right,'d')
scr.onkeypress(left_left,'a')
scr.onkeypress(right_up,'Up')
scr.onkeypress(right_down,'Down')
scr.onkeypress(right_left,'Left')
scr.onkeypress(right_right,'Right')

dx = 5
dy = -5
leftscore = 0
rightscore = 0

while True:
    x = ball.xcor()
    y = ball.ycor()
    ball.setpos(x+dx,y+dy)
    ball.speed(0.02)
    if player_right.distance(ball) < 20:
        dx = -dx
    if player_left.distance(ball) < 20:
        dx = -dx
    if ball.ycor()<-280:
        dy = -dy
    if ball.ycor() > 280:
        dy = -dy
    if ball.xcor() < -450:
        ball.goto(0,0)
        rightpen.clear()
        rightscore = rightscore + 1
        rightpen.write('Rightplayer Score = {}'.format(rightscore),font = ('Courier',20,'bold'))
    if ball.xcor() > 450:
        ball.goto(0,0)
        leftpen.clear()
        leftscore = leftscore + 1
        leftpen.write('Leftplayer Score = {}'.format(leftscore), font=('Courier', 20, 'bold'))

turtle.done()