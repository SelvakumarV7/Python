import turtle

scr = turtle.Screen()
scr.title('Test')
scr.bgcolor('black')

batman_vertices = (0,-3),(1,-1),(2,-2),(3,-1),(4,-2),(7,0),(3,3),(1,1),(1,1.5),(1,3),(0.5,2),(0,2),(-0.5,2),(-1,3),(-1,1.5),(-1,3),(-3,3),(-7,0),(-4,-2),(-3,-1),(-2,-2),(-1,-1)
rhombus_vertices = (-3,-3),(0,-6),(3,-3),(0,0)
star_vertices = (-2,0),(-4,-2.5),(-1,-2),(0,-4.5),(1,-2),(4,-2.5),(2,0),(4,2.5),(1,2),(0,5),(-1,2),(-4,2.5)
scr.register_shape('batman',batman_vertices)
scr.register_shape('rhombus',rhombus_vertices)
scr.register_shape('star',star_vertices)

star = turtle.Turtle()
star.shape('star',)
star.color('yellow')
star.shapesize(10)
star.penup()
star.goto(0,250)


rhombus = turtle.Turtle()
rhombus.shape('rhombus',)
rhombus.color('yellow')
rhombus.shapesize(20)
rhombus.penup()
rhombus.goto(0,-250)

pen = turtle.Turtle()
pen.shape('batman')
pen.color('red')
pen.shapesize(30)
pen.left(90)


turtle.done()