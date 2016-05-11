import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def Ractangle():
    t1.penup()
    t1.pendown()
    t1.setheading(0)
    for i in range(0,4):
        t1.fd(50)
        t1.right(90)
    t1.penup()

def keyup():
    t1.forward(50)

def keyRight():
    t1.right(90)
    

def keyLeft():
    t1.left(90)
    

def keyBack():
    t1.back(50)

def addkeys():
    wn.onkey(keyRight,"Right")
    wn.onkey(keyLeft,"Left")
    wn.onkey(keyBack,"Down")
    wn.onkey(keyup,"Up")

def mousegoto(x,y):
    t1.setpos(x,y)
    t1.pos=(x,y)
    if 100<x<150 and 50<y<100:
        print "correct"

def addMouse():
    wn.onclick(mousegoto)

def lab11():
    t1.penup()
    t1.goto(100,100)
    Ractangle()
    t1.home()
    addkeys()
    addMouse()	
    wn.listen()
    turtle.mainloop()
 

def main():
    lab11()

main()