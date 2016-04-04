import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def drawWindmill((size),(angle),(turns),(bigger)):
	for i in range(turns):
		if i%2==0:
			size=size+bigger
			t1.fd(size)
		else:
			t1.fd(size)
		t1.right(angle)
drawWindmill(10,90,10,5)
wn.exitonclick()