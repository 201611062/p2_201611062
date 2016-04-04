import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

weight=raw_input("Please right your weight (measure is kg) : ")
height=raw_input("Please right your height (measure is m) : ")

weight=float(weight)
height=float(height)

BMI=height/weight*2

def weightMeasure(BMI):
    if BMI<18.5:
        print "Your weight is low"
    elif 18.5<=BMI<=22.9:
        print "Your weight is normal"
    elif 22.9<BMI<=24.9:
        print "Your weight is bit high"
    elif BMI>24.9:
        print "You're OBESITY!!!!"

weightMeasure(BMI)

wn.exitonclick()