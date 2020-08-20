floor=int(input("entre floor number"))
health=input(" entre health is well or not well")
if floor==1:
	if health=="well":
		print("you may go 2nd floor")
	elif health=="not well":
		print("stop here")	
if floor==2:
	if health=="well":
		print("you may go 3rd floor")
	elif health=="not well":
		print("stop here")
if floor==3:
	if health=="well":
		print("you may go 4th floor")
	elif health=="not well":
		print("stop here")
else:
	print("invalid!please entre floor 1 or 2 or 3 and health is well or not well ")
