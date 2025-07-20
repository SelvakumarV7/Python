# Space Fighter Game:
import random
import turtle
import math

score = 0

scr = turtle.Screen()
scr.title('Space Fighter')
scr.bgcolor('black')
scr.setup(800,800)
scr.tracer(0)

# to register shapes:

player_vertices = ((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18,5),(15,0))
scr.register_shape('player',player_vertices)
asteroid_vertices = ((0,10),(5,7),(3,3),(10,0),(7,4),(8,-6),(0,-10),(-5,-5),(-7,-7),(-10,0),(-5,4),(-1,8))
scr.register_shape('asteroid',asteroid_vertices)

# to create Player:

player = turtle.Turtle()
player.shape('player')
player.shapesize(2)
player.color('white')
player.goto(0,0)

def player_left():
    player.lt(10)
def player_right():
    player.rt(10)



# to create enemy:

def get_heading_to(t1,t2):
    x1 = t1.xcor()
    y1 = t1.ycor()

    x2 = t2.xcor()
    y2 = t2.ycor()

    heading = math.atan2(y1-y2,x1-x2)
    heading = heading*180/3.14159
    return heading

no_of_asteroid = 5
asteroids = []
for i in range(no_of_asteroid):
    asteroid = turtle.Turtle()
    asteroid.shape('asteroid')
    asteroid.shapesize(1.7)
    asteroid.color('red')
    asteroid.penup()
    asteroid.goto(0,0)
    asteroid.speed = random.randint(2,10)/100
    heading = random.randint(0,360)
    distance = random.randint(400,600)
    asteroid.setheading(heading)
    asteroid.forward(distance)
    asteroids.append(asteroid)
    asteroid.setheading(get_heading_to(player,asteroid))

# to create missile:

no_of_missile = 3
missiles = []
for i in range(no_of_missile):
    missile = turtle.Turtle()
    missile.shape('triangle')
    missile.color('brown')
    missile.penup()
    missile.goto(100,100)
    missiles.append(missile)
    missile.speed = 1
    missile.state = 'ready'
    missile.hideturtle()


def fire_missile():
    for missile in missiles:
        if missile.state == 'ready':
            missile.goto(0,0)
            missile.showturtle()
            missile.setheading(player.heading())
            missile.state = 'fire'
            break



# to create ScoreBoard:

sb = turtle.Turtle()
sb.shape('square')
sb.color('yellow')
sb.penup()
sb.goto(0,350)
sb.write('Score = 0',align = 'center',font = ('Arial',20,'bold'))
sb.hideturtle()


scr.listen()
scr.onkeypress(player_left,'a')
scr.onkeypress(player_right,'d')
scr.onkeypress(fire_missile,'space')


while True:
    scr.update()
    player.goto(0,0)
    for missile in missiles:
        if missile.state == 'fire':
            missile.forward(missile.speed)
        if missile.xcor()>400 or missile.xcor()<-400 or missile.ycor()>400 or missile.ycor()<-400:
            missile.hideturtle()
            missile.state = 'ready'

    for asteroid in asteroids:
        asteroid.forward(asteroid.speed)

        for missile in missiles:
            if asteroid.distance(missile)<20:
                heading = random.randint(0, 360)
                distance = random.randint(400, 600)
                asteroid.setheading(heading)
                asteroid.forward(distance)
                asteroid.setheading(get_heading_to(player, asteroid))

                missile.goto(1000,1000)
                missile.hideturtle()
                missile.state='ready'

                score+=10
                sb.clear()
                sb.write('Score = {}'.format(score),align = 'center',font = ('arial',20,'bold'))

            if asteroid.distance(player)<30:
                print('Game over!')
                exit()


turtle.done()