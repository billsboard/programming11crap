import turtle as t
import random as r
import sys
import math
from mathPoint import *
import time
import os

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


if("idlelib" in sys.modules):
    print("Warning: Program running in idle, auto-restart will not work")
    abort = sc.textinput("Warning", "Program has been launched by idle and not\
 from terminal/shell.\nAuto-restart feature will be non-functional. Continue?\
 (default is \"N\")").lower()
    if(not ("y" in abort or "sure" in abort)):
        sc.bye()
        sys.exit()

counter = t.Turtle()
t.ht()
counter.ht()
counter.write("3", font=("Helvetica","25"))
time.sleep(1)
counter.clear()
counter.write("2", font=("Helvetica","25"))
time.sleep(1)
counter.clear()
counter.write("1", font=("Helvetica","25"))
time.sleep(1)
counter.clear()
counter.penup()
t.st()


def hitWall():
    global flag
    global gen
    stopListening()
    gen.ht()
    t.clear()
    t.penup()
    t.goto(-180,0)
    t.pendown()
    t.ht()
    t.write("You hit a wall! Final score was: %d" % scoreCount, font=("Helvetica",24))
    t.penup()
    flag=False
    time.sleep(1)
    processAnswer(sc.textinput("Snake prompt", "Would you like to play again?"))
def gameover():
    global flag
    global gen
    stopListening()
    gen.ht()
    t.clear()
    t.penup()
    t.clear()
    t.goto(-200,0)
    t.pendown()
    t.ht()
    t.write("Game Over! Your final score was: %d" % scoreCount, font=("Helvetica",24))
    t.penup()
    flag=False
    time.sleep(1)
    processAnswer(sc.textinput("Snake prompt", "Would you like to play again?"))
def processAnswer(answer):
    answer = answer.lower()
    if( "sure" in answer or "y" in answer):
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif("n" in answer):
        exit()
    else:
        processAnswer(sc.textinput("Snake prompt", "Please answer \"yes\" or \"no\"")) 
def exit():
    sc.bye()
    sys.exit()

lastPoint = (0,0)

def upKey():
    global lastPoint
    global loc
    coords = (t.xcor(), t.ycor())
    loc.append(Line(Point(lastPoint), Point(coords)))
    lastPoint = coords
    if(t.heading() == 270):
        gameover()
    stopListening()
    t.setheading(90)
    t.fd(3)
    startListening()

def downKey():
    global lastPoint
    global loc
    coords = (t.xcor(), t.ycor())
    loc.append(Line(Point(lastPoint), Point(coords)))
    lastPoint = coords
    if(t.heading() == 90):
        gameover()
    stopListening()
    t.setheading(270)
    t.fd(3)
    startListening()

def leftKey():
    global lastPoint
    global loc
    coords = (t.xcor(), t.ycor())
    loc.append(Line(Point(lastPoint), Point(coords)))
    lastPoint = coords
    if(t.heading() == 0):
        gameover()
    stopListening()
    t.setheading(180)
    t.fd(3)
    startListening()

def rightKey():
    global lastPoint
    global loc
    coords = (t.xcor(), t.ycor())
    loc.append(Line(Point(lastPoint), Point(coords)))
    lastPoint = coords
    if(t.heading() == 180):
        gameover()
    stopListening()
    t.setheading(0)
    t.fd(3)
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

def play():
    global lastPosition
    global itemExists
    global scoreCount
    while(flag):
        currentLocation = Point((t.xcor(), t.ycor()))
        for l in loc:
            if(l.onLine(currentLocation)):
                gameover()

    
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
        movedLocation = Point((t.xcor(), t.ycor()))

        for l in loc:
            if(t.heading() == 90):
                if(l.intersect(Line(movedLocation, Point((t.xcor(), movedLocation.y - 2.9))))):
                    gameover()
            elif(t.heading() == 270):
                if(l.intersect(Line(movedLocation, Point((t.xcor(), movedLocation.y + 2.9))))):
                    gameover()
            elif(t.heading() == 180):
                if(l.intersect(Line(movedLocation, Point((movedLocation.x - 2.9, t.ycor()))))):
                    gameover()
            else:
                if(l.intersect(Line(movedLocation, Point((movedLocation.x + 2.9, t.ycor()))))):
                    gameover()


play()

