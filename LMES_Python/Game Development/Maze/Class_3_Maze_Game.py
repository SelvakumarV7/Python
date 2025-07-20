import turtle

space = turtle.Screen()
rocket = turtle.Turtle()
spaceman = turtle.Turtle()

space.bgpic('background.gif')

space.addshape('rocket.gif')
space.addshape('rocket_left.gif')
space.addshape('rocket_down.gif')
space.addshape('rocket_right.gif')

rocket.shape('rocket.gif')
rocket.penup()
rocket.goto(180,-250)

space.addshape('spaceman.gif')
spaceman.shape('spaceman.gif')
spaceman.penup()
spaceman.goto(-100,260)

def up():
    rocket.setheading(90)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape('rocket.gif')

def down():
    rocket.setheading(270)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape('rocket_down.gif')

def left():
    rocket.setheading(180)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape('rocket_left.gif')

def right():
    rocket.forward(10)
    rocket.shape('rocket_right.gif')

space.listen()

space.onkeypress(up,'w')
space.onkeypress(down,'s')
space.onkeypress(left,'a')
space.onkeypress(right,'d')

while True:
    space.update()
    if rocket.distance(spaceman)<20:
        space.bgpic('win.gif')

turtle.done()