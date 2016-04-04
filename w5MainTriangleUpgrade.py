import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

size=raw_input("Right number then I'll make you triangle!! : ")

size=int(size)

def makeTriangle(size):
    for i in range(size):
        print " "*(size-i)+"#"*(i*2-1)

makeTriangle(size)

wn.exitonclick()