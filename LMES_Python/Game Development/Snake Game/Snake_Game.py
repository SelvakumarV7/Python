# Snake Game:

import turtle
import random

score = 0
segment = []

scr = turtle.Screen()
scr.bgpic('grass.gif')

#scr.tracer(0)

scr.addshape('body.gif')
scr.addshape('left.gif')
scr.addshape('right.gif')
scr.addshape('up.gif')
scr.addshape('down.gif')

snake = turtle.Turtle()
snake.setheading(90)
snake.speed(4)
snake.penup()
snake.shape('up.gif')


food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.speed(100)
food.penup()
food.goto(100,100)

sb = turtle.Turtle()
sb.penup()
sb.goto(0,240)
sb.hideturtle()
sb.color('black')
sb.write('Score = 0',align = 'center', font = ('Arial',22,'bold'))


def move():
    snake.forward(10)

def up():
    if snake.heading() != 270:
        snake.setheading(90)
        snake.shape('up.gif')

def down():
    if snake.heading() != 90:
        snake.setheading(270)
        snake.shape('down.gif')

def left():
    if snake.heading() != 0:
        snake.setheading(180)
        snake.shape('left.gif')

def right():
    if snake.heading() != 180:
        snake.setheading(0)
        snake.shape('right.gif')

scr.listen()
scr.onkeypress(up,'w')
scr.onkeypress(down,'s')
scr.onkeypress(left,'a')
scr.onkeypress(right,'d')

while True:
    scr.update()

    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        scr.bgpic('game_over.gif')
        food.hideturtle()
        snake.hideturtle()
    for i in segment:
        if i.distance(snake)<5:
            scr.bgpic('game_over.gif')
            food.hideturtle()
            snake.hideturtle()

    if snake.distance(food) < 10:
        x = random.randint(-220,220)
        y = random.randint(-220,220)
        food.setpos(x,y)

        score += 10
        sb.clear()
        sb.write('Score = {}'.format(score), align='center', font=('Arial', 22, 'bold'))

        body = turtle.Turtle()
        body.shape('body.gif')
        body.speed(0)
        body.penup()
        segment.append(body)

    for i in range(len(segment) -1, 0, -1):
        x = segment[i - 1].xcor()
        y = segment[i - 1].ycor()
        segment[i].goto(x,y)

    if len(segment) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segment[0].goto(x,y)
    move()




turtle.done()