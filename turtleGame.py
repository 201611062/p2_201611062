import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
import random

def gotoRandom():
    t1.penup()
    x=random.randrange(-200,200)
    y=random.randrange(-300,300)
    t1.goto(x,y)
    t1.pendown()

def Triangle():
    t1.penup()
    t1.pendown()
    t1.setheading(0)
    for i in range(0,3):
        t1.right(120)
        t1.fd(50)
    t1.penup()

def Star():
    t1.penup()
    t1.pendown()
    t1.setheading(0)
    for i in range(0,5):
        t1.right(144)
        t1.fd(50)
    t1.penup()

def Ractangle():
    t1.penup()
    t1.pendown()
    t1.setheading(0)
    for i in range(0,4):
        t1.fd(50)
        t1.right(90)
    t1.penup()

def final():
    print "                      Let'Play Turtle Game!"
    print ""
    print "                          ---RULE---                              "
    print "###################################################################"
    print "# You have to put turtle inside the shape in three times.         #"
    print "# Each time you put turtle inside the shape, you can get 10 point.#"
    print "# And I'll give you 5 chance! Good luck!!                         #"  
    print "###################################################################"
    print ""
    global point
    global question
    global time
    point=0
    #그림그리는 함수
    for i in range(0,5):
            time=3
            t1.home()
            t1.clear()
	    t1.color("black")
            gotoRandom()
            pos=t1.pos()
            z=random.randrange(0,3)
            if z==0:
                Ractangle()
            elif z==1:
                Star()
            elif z==2:
                Triangle()
            gotoRandom()

            #이제부터 움직임

            #방향조정
            for i in range(0,3):
                t1.shape("turtle")
		t1.color("green")
                heading=raw_input("Turn right or left or just stay? : ")
                if heading=="right":
                    how=input("How much? : ")
                    t1.right(how)
                elif heading=="left":
                    how=input("How much : ")
                    t1.left(how)
                elif heading=="stay":
                    t1.fd(0)
                fd=input("How much do you want to go? :")
                t1.fd(fd)
                question=raw_input("Where is your turtle? Inside or outside? : ")
                if question=="inside":
                    break
                elif question=="outside":
                    time=time-1
                    t=str(time)
                    if time==0:
                        print "Over"
                    else:
                        print t+" time left"
                    
            if question=="inside":
                print "I'll give you 10point"
                point=point+10
                p=str(point)
                print "Your score is now "+p
            elif question=="outside":
                print "You lost the chance"
                p=str(point)
                print "Your score is now "+p
    print ""
    print ""            
    if point<30:
        print "You got "+p+"point"
	print "You are Lose Ha Ha"
    elif point>=30:
	print "You got "+p+"point"
        print "Good job! You are Winner"
    wn.exitonclick()

final()

