# Coin_hunter Game:

import turtle
import random

score = 0

scr = turtle.Screen()
scr.bgpic('screen.gif')


scr.addshape('left.gif')
scr.addshape('right.gif')
scr.addshape('coin.gif')

player = turtle.Turtle()
player.shape('left.gif')
player.penup()
player.goto(0,-150)

coin = turtle.Turtle()
coin.shape('coin.gif')
coin.penup()
coin.goto(-280,280)
coin.speed(5)

scoreboard = turtle.Turtle()
scoreboard.shape('square')
scoreboard.penup()
scoreboard.goto(-50,240)
scoreboard.write('Score = 0',font = ('Arial',20,'bold'))
scoreboard.hideturtle()

def player_left():
    player.shape('left.gif')
    player.backward(5)

def player_right():
    player.shape('right.gif')
    player.forward(5)

scr.listen()
scr.onkeypress(player_left,'a')
scr.onkeypress(player_right,'d')

def coin_move():
    y = coin.ycor()
    coin.sety(y-2)

while True:
    scr.update()
    coin_move()
    if coin.ycor() < -280:
        x = random.randint(-280,280)
        coin.goto(x,280)
    if player.distance(coin )< 50:
        coin.hideturtle()
        x = random.randint(-280, 280)
        coin.goto(x, 280)
        coin.showturtle()
        score += 10
        scoreboard.clear()
        scoreboard.write('Score = {}'.format(score), font=('Arial', 20, 'bold'))


turtle.done()