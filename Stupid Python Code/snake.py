import turtle as t
import random as r
import sys
import math
import mathPoint as mp

flag = True

t.color("blue")
sc = t.Screen()
t.speed(0)
sc.screensize(500,500)

score = t.Turtle()
score.speed(0)
score.penup()
score.goto(250,300)
score.ht()
score.write("Score: 0", font=("Helvetica",18))

writer = t.Turtle()
writer.speed(0)
writer.penup()
writer.ht()
writer.goto(-300, 300)
writer.pendown()
writer.write("A Normal Snake Game by Bill Wang", font=("Helvetica",18))

border = t.Turtle()
border.speed(0)
border.penup()
border.goto(-400,290)
border.pendown()
border.fd(800)

    
def hitWall():
    global flag
    global gen
    gen.ht()
    t.clear()
    t.penup()
    t.goto(-180,0)
    t.pendown()
    t.ht()
    t.write("You hit a wall! Final score was: %d" % scoreCount, font=("Helvetica",24))
    t.penup()
    flag=False
    stopListening()
def gameover():
    global flag
    global gen
    gen.ht()
    t.clear()
    t.penup()
    t.goto(-200,0)
    t.pendown()
    t.ht()
    t.write("Game Over! Your final score was: %d" % scoreCount, font=("Helvetica",24))
    t.penup()
    flag=False
    stopListening()
def exit():
    sc.bye()
    sys.exit()
def upKey():
    if(t.heading() == 270):
        gameover()
    stopListening()
    t.setheading(90)
    startListening()

def downKey():
    if(t.heading() == 90):
        gameover()
    stopListening()
    t.setheading(270)
    startListening()

def leftKey():
    if(t.heading() == 0):
        gameover()
    stopListening()
    t.setheading(180)
    startListening()

def rightKey():
    if(t.heading() == 180):
        gameover()
    stopListening()
    t.setheading(0)
    startListening()

def stopListening():
    sc.onkey(None, "Left")
    sc.onkey(None, "Right")
    sc.onkey(None, "Up")
    sc.onkey(None, "Down")
    sc.onkey(None, "a")
    sc.onkey(None, "d")
    sc.onkey(None, "w")
    sc.onkey(None, "s")

def startListening():
    sc.onkey(leftKey, "Left")
    sc.onkey(rightKey, "Right")
    sc.onkey(upKey, "Up")
    sc.onkey(downKey, "Down")
    sc.onkey(leftKey, "a")
    sc.onkey(rightKey, "d")
    sc.onkey(upKey, "w")
    sc.onkey(downKey, "s")

startListening()

sc.listen()

# Code for direction changing
itemExists = False

gen = t.Turtle()
loc = []
scoreCount = 0

def genSquare():
    global itemExists
    global gen
    x = r.randint(-325, 325)
    y = r.randint(-325, 270)
    gen.speed(0)
    gen.penup()
    gen.goto(x,y)
    gen.shape("square")
    gen.color("red")
    gen.st()
    itemExists = True
"""
def play():
    global itemExists
    global scoreCount
    while(flag):
        coords = [t.xcor(), t.ycor()]
        coordx1 = [t.xcor()-1, t.ycor()]
        coordx2 = [t.xcor()-2, t.ycor()]
        if coords in loc or coordx1 in loc or coordx2 in loc:
            gameover()
    
        loc.append(coords)
        if(not itemExists):
            genSquare()
        if(t.distance(gen) < 15):
            gen.ht()
            score.clear()
            scoreCount += 1
            score.write("Score: %d" % scoreCount, font=("Helvetica",18))
            itemExists = False
        if(t.xcor() >= 350 or t.xcor() <= -355 or t.ycor() >= 290 or t.ycor() <= -333):
            hitWall()
        t.fd(3)
"""
def play():
    global lastPosition
    global itemExists
    global scoreCount
    while(flag):
        coords = [t.xcor(), t.ycor()]
        coordx1 = [t.xcor()-1, t.ycor()]
        coordx2 = [t.xcor()-2, t.ycor()]
        
        if coords in loc or coordx1 in loc or coordx2 in loc:
            gameover()
    
        loc.append(coords)
        if(not itemExists):
            genSquare()
        if(t.distance(gen) < 15):
            gen.ht()
            score.clear()
            scoreCount += 1
            score.write("Score: %d" % scoreCount, font=("Helvetica",18))
            itemExists = False
        if(t.xcor() >= 350 or t.xcor() <= -355 or t.ycor() >= 290 or t.ycor() <= -333):
            hitWall()
        t.fd(3)


play()
