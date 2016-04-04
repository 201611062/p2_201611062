import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

print "Let's start Rock Sissor Paper"

Boy=raw_input("What boy show?? :")
Girl=raw_input("What girl show?? :")

def winner((Boy), (Girl)):
	if(Boy==Girl):
		print "Draw"
	elif(Boy=="Rock"):
		if(Girl=="Sissor"):
			print "Boy Win!!"
		elif(Girl=="Paper"):
			print "Girl Win!!"
	elif(Boy=="Sissor"):
		if(Girl=="Rock"):
			print "Girl Win!!"
		elif(Girl=="Paper"):
			print "Boy Win!!"
	elif(Boy=="Paper"):
		if(Girl=="Rock"):
			print "Boy Win!!"
		elif(Girl=="Sissor"):
			print "Girl Win!!"
	else:
		print "Do it again"

winner(Boy, Girl)

print "Game Over"

wn.exitonclick()