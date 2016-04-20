import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def saveTracks():
    mytracks=list()
    t1.speed(1)
    t1.penup()
    t1.goto(-400,300)
    mytracks.append(t1.pos())
    t1.pencolor("Red")
    t1.right(90)
    t1.fd(400)
    mytracks.append(t1.pos())
    t1.backward(150)
    mytracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    mytracks.append(t1.pos())
    t1.left(90)
    t1.fd(300)
    mytracks.append(t1.pos())
    t1.back(150)
    mytracks.append(t1.pos())
    t1.right(90)
    t1.fd(300)
    mytracks.append(t1.pos())
    t1.left(90)
    t1.right(90)
    t1.right(90)
    t1.fd(200)
    mytracks.append(t1.pos())
    t1.fd(300)
    mytracks.append(t1.pos())
    t1.back(100)
    mytracks.append(t1.pos())
    t1.left(90)
    t1.fd(200)
    mytracks.append(t1.pos())
    t1.goto(mytracks[0])
    t1.pendown()

def replayTracks(mytracks):
    for i in range(0,len(mytrakcs)):
        t1.goto(mytracks)

def lab7():
    mytracks=saveTracks()
    replayTracks(mytracks)

def main():
    lab7()

main()