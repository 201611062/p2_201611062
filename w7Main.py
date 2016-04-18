import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
import random


def drawSquareAtSave(size, pos): 
    t1.penup() 
    t1.setpos(pos) 
    t1.pendown()
    tracks=list()
    for i in range(0,4): 
        tracks.append(t1.pos())
        t1.forward(size) 
        t1.right(90)
    return tracks

def gotoRandom():
    t1.penup()
    x=random.randrange(-200,200)
    y=random.randrange(-300,300)
    t1.goto(x,y)
    t1.pendown()

def drawSquareFrom():
    gotoRandom()
    tracks=list()
    t1.penup()
    t1.setheading(0)
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.fd(100)
        t1.right(90)
    t1.home()
    t1.pendown()
    for i in range(0,4):
        t1.goto(tracks[i])
    t1.goto(tracks[0])

def lab7():
    size=100
    pos=(100,100)
    myTrack=drawSquareAtSave(size,pos)
    print myTrack
    drawSquareFrom()

def main():
    lab7()

#두번째 문제에 argument가 없는 이유는 tracks를 임의로 컴퓨터가 지정하기 때문에 입력할 필요가 없습니다.
main()
