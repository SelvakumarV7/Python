# Game Development:
import random
import turtle

score = 0


scr = turtle.Screen()
scr.title('Space Invaders')
scr.bgpic('space.gif')
scr.setup(800,800)
scr.tracer(0)                   # animations are hidden here

# to register image files

scr.register_shape('player.gif')
scr.register_shape('enemy.gif')
scr.register_shape('bullet.gif')


# to create player:

player = turtle.Turtle()
player.shape('player.gif')
player.penup()
player.goto(0,-280)


#to create Enemy:

no_of_enemies = 5
enemies = []
for i in range(no_of_enemies):
    enemy = turtle.Turtle()
    enemy.shape('enemy.gif')
    enemy.penup()
    x = random.randint(-260,260)
    y = random.randint(140,260)
    enemy.goto(x,y)
    enemies.append(enemy)

enemyspeed = 0.05


#to create Bullet:

bullet = turtle.Turtle()
bullet.shape('bullet.gif')
bullet.penup()
bullet.goto(0,-240)
bullet.hideturtle()


bulletspeed = 0.5
bulletstate = 'ready'           #ready - it is ready to shoot, # fire = bullet is in travel



# to create scoreboard:

sb = turtle.Turtle()
sb.shape('square')
sb.color('black')
sb.penup()
sb.goto(0,350)
sb.write('Score = 0',align = 'center',font = ('Ariel',20,'bold'))
sb.hideturtle()


# to Create Functions:

def player_left():
    x = player.xcor()
    x-=20
    if x<-250:
        x = -250
    player.setx(x)

def player_right():
    x = player.xcor()
    x+=20
    if x > 250:
        x = 250
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'fire'
        x = player.xcor()
        y = player.ycor()+40
        bullet.goto(x,y)
        bullet.showturtle()



scr.listen()
scr.onkeypress(player_left,'a')
scr.onkeypress(player_right,'d')
scr.onkeypress(fire_bullet,'space')


while True:             # infinite Loop
    scr.update()
    for enemy in enemies:
        x = enemy.xcor()
        x+=enemyspeed
        if x > 260:
            for e in enemies:
                y = e.ycor()
                y-=30
                e.sety(y)
                enemyspeed*=-1
        if x < -260:
            for e in enemies:
                y = e.ycor()
                y-=30
                e.sety(y)
                enemyspeed*=-1
        enemy.setx(x)

        if bullet.distance(enemy)<20:
            bullet.hideturtle()
            bullet.goto(1200,1200)
            x = random.randint(-260, 260)
            y = random.randint(140, 260)
            enemy.goto(x, y)
            score+=10
            sb.clear()
            sb.write('score = {}'.format(score),align = 'center',font = ('arial',20,'bold'))

        if enemy.distance(player)<20:
            print('''You Lost  ---   Game Over''')
            exit()


    if bulletstate == 'fire':
        y = bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)

    if bullet.ycor()>370:
        bullet.hideturtle()
        bulletstate = 'ready'



turtle.done()