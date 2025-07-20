import turtle

road = turtle.Screen()
road.bgpic('track.gif')

road.addshape('redcar.gif')
road.addshape('bluecar.gif')

redcar = turtle.Turtle()
redcar.penup()
redcar.goto(-100,-240)
redcar.setheading(90)
redcar.shape('redcar.gif')

bluecar = turtle.Turtle()
bluecar.penup()
bluecar.goto(100,-240)
bluecar.setheading(90)
bluecar.shape('bluecar.gif')


def player1():
    redcar.forward(5)

def player2():
    bluecar.forward(5)

road.listen()
road.onkeypress(player1,'w')
road.onkeypress(player2,'Up')

while True:
    road.update()
    if redcar.position() > (-100,200):
        road.bgpic('redcar_win.gif')
    if bluecar.pos() > (100,200):
        road.bgpic('bluecar_win.gif')
turtle.done()

