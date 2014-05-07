def quit (window):
	window.destroy ()

def readjust (widget, name):
	x = input ("Relative x: " )
	y = input ("Relative y: " )
	
	if x <= 1 and x >= 0 and y <=1 and y >=0:
		ht = input ("Height: " )
		wd = input ("Width: " )
		widget.place (relx = x, rely = y, height = ht, width = wd)
				
		choice =  raw_input ("Do you want to readjust? Y/N: " )
		if choice == 'Y' or choice == 'y':
			assign (widget, name)
		elif choice == 'N' or choice == 'n':
			code = name + ".place (relx = " + str (x) + ", rely = " + str (y) + ", height = " + str (ht) + ", width = " + str (wd) + ")"
			print code
			print "K"
			quit (widget.master)
			
		else:
			print "Invalid choice"
			quit (widget.master)
		
	else:
		if x > 1 or x < 0 and y > 1 or y < 0:
			print "Check both values"
		else:
			if x > 1 or x < 0:
				print "Check value of x" 
			
			elif y > 1 or y < 0:
				print "Check value of y"
				 
		quit (widget.master)
