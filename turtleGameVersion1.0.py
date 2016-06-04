import turtle
t1=turtle.Turtle()
wn=turtle.Screen()

import random
import math

def mousegoto(x,y):
    t1.setpos(x,y)
    cp=t1.pos()
    p=[x1,y1]
    circleRed(cp,p,radius,level)
    timeFunction(time,level)
    time-=1

def addMouse():
    wn.onclick(mousegoto)

def circleRed(cp,p,radius,level):
    if math.sqrt(math.pow(cp[0]-p[0],2)+math.pow(cp[1]-(p[1]+radius),2))<=radius:
        t1.goto(p[0],p[1])
        t1.pendown()
        t1.fillcolor("Red")
        t1.begin_fill()
        t1.setheading(0)
        t1.circle(radius)
        t1.end_fill()
        t1.penup()
        t1.home()
        t1.clear()
        startGlobal(level)

def timeFunction(time,level):
    if time>0:
        print str(time)+" time left"
        
        time-=1
    elif time==0:
        print "game over"
        wn.exitonclick()
def startGlobal(level):
    global radius
    global x1
    global y1
    global x
    global time
    level+=1
    print "Level"+str(level)
    x1=random.randrange(-200,200)
    y1=random.randrange(-300,300)
    meno=open("turtle.txt",'r')
    x=[int(meno.readline())]
    meno.close()
    radius=x[0]-level*30

def firtStart():
    global level
    level=1
    print "Level"+str(level)
    
    addMouse()
    startGlobal(level)
    wn.listen()
    turtle.mainloop()

firtStart()