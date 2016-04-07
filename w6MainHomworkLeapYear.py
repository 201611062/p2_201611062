#남자가 술래입니다.
	Boy=raw_input("Boy choose the number : ")
	times=raw_input("How many times do you want to give opportunity? : ")
	Boy=int(Boy)

	times=int(times)

	def updownGame((Boy),(times)):
    		for i in range(times):
        		Girl=raw_input("Girl choose the number : ")
			Girl=int(Girl)
        		if Boy>Girl :
            			print "Finger Up"
        		elif Boy<Girl :
            			print "Finger Down"
        		elif Boy==Girl:
            			print "That's right"
	    			print "Gamve over. Girl win!!"
            			wn.exitonclick()
	

	updownGame(Boy,times)
	print "Game over. Boy win!!"
	wn.exitonclick()