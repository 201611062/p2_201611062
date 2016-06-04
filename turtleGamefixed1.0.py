import turtle
t1=turtle.Turtle()
wn=turtle.Screen()
import random
import math

def mousegoto(x,y):
    t1.setpos(x,y)
    cp=t1.pos()
    p=[x1,y1]
    circleRed(cp,p)
    timeFunction(cp,p)

def addMouse():
    wn.onclick(mousegoto)

def radius():
    meno1=open("level.txt","r")
    l=[int(meno1.readline())]
    meno1.close()
    level=l[0]
    meno2=open("radius.txt","r")
    i=[int(meno2.readline())]
    meno2.close()
    radius=i[0]
    radius=radius-level*30
    meno2=open("radius.txt","w")
    meno2.write(str(radius))
    meno2.close()

def circleRed(cp,p):
    meno2=open("radius.txt","r")
    i=[int(meno2.readline())]
    meno2.close()
    radius=i[0]
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
        timeReset()
	t1.color("black")
	t1.pendown()
        startGlobal()

def circleRedEnd(cp,p):
    meno2=open("radius.txt","r")
    i=[int(meno2.readline())]
    meno2.close()
    radius=i[0]
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
    timeReset()
    t1.color("black")
    t1.pendown()

def timeFunction(cp,p):
    timeDown()
    meno1=open("time.txt","r")
    l=[int(meno1.readline())]
    meno1.close()
    time=l[0]
    if time>0:
        print str(time)+" time left"
    elif time==0:
        print "game over"
	circleRedEnd(cp,p)
        score()
        restart()
        wn.exitonclick()

def startGlobal():
    global x1
    global y1
    levelUp()
    meno1=open("level.txt","r")
    l=[int(meno1.readline())]
    meno1.close()
    print "Level "+str(l[0])
    print ""
    x1=random.randrange(-100,100)
    y1=random.randrange(-200,200)
    radius()

def firtStart():
    addMouse()
    startGlobal()
    wn.listen()
    turtle.mainloop()

def levelUp():
    meno1=open("level.txt","r")
    l=[int(meno1.readline())]
    meno1.close()
    l[0]+=1
    meno2=open("level.txt",'w')
    meno2.write(str(l[0]))
    meno2.close()

def timeDown():
    meno1=open("time.txt","r")
    l=[int(meno1.readline())]
    meno1.close()
    l[0]-=1
    meno2=open("time.txt",'w')
    meno2.write(str(l[0]))
    meno2.close()

def timeReset():
    meno2=open("time.txt",'w')
    meno2.write("11")
    meno2.close()

def restart():
    meno2=open("level.txt",'w')
    meno2.write("0")
    meno2.close()
    meno2=open("radius.txt",'w')
    meno2.write("300")
    meno2.close()
    meno2=open("time.txt",'w')
    meno2.write("11")
    meno2.close()

def score():
    x=list()
    meno=open("score.txt","r")
    for line in meno:
        x.append(line.split())
    meno.close()
    y=list()
    for i in x:
        y.append(int(i[2]))
    z=list()
    for i in x:
        z.append([i[1],i[2]])
    meno1=open("level.txt","r")
    l=[int(meno1.readline())]
    meno1.close()
    p=l[0]
    initial=raw_input("Your initial : ")
    q=[initial,p]
    ha=0
    r=list()
    i=0
    while ha!=1:
        if p>y[i]:
            r.append(q)
            ha=1
        else:
            if p==y[i]:
                if y[i-1]>y[i]:
                    r.append(q)
                    ha=1
                else:
                    r.append(z[i])
                    if len(r)==10:
                        ha=1
            else:
                r.append(z[i])
                if len(r)==10:
                        ha=1
        i+=1

    t=len(r)
    for i in range(10-t):
        r.append(z[i+t-1])
    meno=open("score.txt","w")
    for i in range(10):
        meno.write(str(i+1)+"\t"+r[i][0]+"\t"+str(r[i][1])+"\n")
    meno.close()
    meno=open("score.txt","r")
    for line in meno:
        print line
    meno.close()
    

firtStart()