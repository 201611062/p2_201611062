import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

grade=raw_input("your grade please:")

marks=float(grade)

def yourGrade(marks):
    if(90<=marks<=100):
        grade="A"
        print "your grade is "+(grade)
    elif(80<=marks<90):
        grade="B"
        print "your grade is "+(grade)
    elif(70<=marks<80):
        grade="C"
        print "your grade is "+(grade)
    elif(60<=marks<70):
        grade="D"
        print "your grade is "+(grade)
    else:
        print "your grade is F"

yourGrade(marks)

wn.exitonclick()