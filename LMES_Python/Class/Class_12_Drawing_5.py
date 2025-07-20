# Chick Game:

import turtle

scr = turtle.Screen()
scr.title('Chick demo')
scr.bgpic('chick_2.gif')
scr.setup(800,800)

scr.register_shape('chick_1.gif')
chick = turtle.Turtle()
chick.shape('chick_1.gif')


turtle.done()