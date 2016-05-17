import turtle
import math
wn=turtle.Screen()
t1=turtle.Turtle()

def keyup():
    t1.forward(50)
    pos=t1.pos()
    pt=t1.pos()
    line=t1.pos()
    CircleRed(pos,radius)
    isInRectangle(pt,coord)
    onLine(line)
    
def keydown():
    t1.backward(50)
    pos=t1.pos()
    pt=t1.pos()
    line=t1.pos()
    CircleRed(pos,radius)
    isInRectangle(pt,coord)
    onLine(line)
    
def keyleft():
    t1.left(90)

def keyright():
    t1.right(90)

def mousegoto(x,y):
    t1.setpos(x,y)
    pos=t1.pos()
    pt=t1.pos()
    line=t1.pos()
    CircleRed(pos,radius)
    isInRectangle(pt,coord)
    onLine(line)

def addKeys():
    wn.onkey(keyup,"Up")
    wn.onkey(keydown,"Down")
    wn.onkey(keyright,"Right")
    wn.onkey(keyleft,"Left")

def addMouse():
    wn.onclick(mousegoto)

def Ractangle(xs,ye):
    t1.penup()
    t1.goto(xs,ye)
    t1.pendown()
    t1.setheading(0)
    for i in range(0,4):
        t1.fd(ye-xs)
        t1.right(90)
    t1.penup()
    t1.home()
    
def isInRectangle(pt,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    if(xs<=pt[0]<=xe and ys<=pt[1]<=ye or -ye<=pt[0]<=-xs and ys<=pt[1]<=xe):
        RactangleRed(xs,ye)
            


    
def RactangleRed(xs,ye):
    t1.penup()
    t1.goto(xs,ye)
    t1.pendown()
    t1.fillcolor("Red")
    t1.begin_fill()
    t1.setheading(0)
    for i in range(0,4):
        t1.fd(ye-xs)
        t1.right(90)
    t1.end_fill()
    t1.penup()
    homeclear()
    drawLineAt(pos1,pos2)

def onLine(line):
    if(x1<=line[0]<=x2 and y1<=line[1]<=y1+1 or -y1-1<=line[0]<=-x1 and y+1<=line[1]<=x2):
        print "On Line"
        homeclear()
        isInCircle(radius,circlepos)

def drawLineAt(pos1,pos2):
    t1.penup()
    t1.goto(pos1)
    t1.pendown()
    t1.goto(pos2)
    t1.penup()
    t1.home()

def isInCircle(radius,circlepos):
    t1.penup()
    t1.goto(circlepos)
    t1.pendown()
    t1.circle(radius)
    t1.penup()
    t1.home()
    

def CircleRed(pos,radius):
    if math.sqrt(math.pow(center[0]-pos[0],2)+math.pow(center[1]-pos[1],2))<=radius:
        t1.goto(circlepos)
        t1.pendown()
        t1.fillcolor("Red")
        t1.begin_fill()
        t1.setheading(0)
        t1.circle(radius)
        t1.end_fill()
        t1.penup()
        homeclear()
        wn.bgpic("C:\Users\S540\Desktop\myMaze.gif")

def homeclear():
    t1.home()
    t1.clear()

print "Implement the program after wirting"
xs=input("Wirte xs : ")
xe=input("Wirte xe, xe has to bigger than xs : ")
ys=xs
ye=xe
coord=[(xs,ys),(xe,ye)]    
Ractangle(xs,ye)

x1=input("Write point x1 : ")
y1=input("Write point y1 : ")
x2=input("Write point x2, x2 has to bigger than x1 : ")
pos1=(x1,y1)
pos2=(x2,y1)


x=input("Write x : ")
y=input("Write y : ")
circlepos=(x,y)
radius=input("Write radius : ")
center=(x,y+radius)


addKeys()
addMouse()
wn.listen()
turtle.mainloop()