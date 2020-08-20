room_member=int(input("entre any number"))
if room_member>8:
	print("shift to another room girls",room_member-8)
elif room_member<8:
	print("shift from another room girls",8-room_member)
else:
	print("no more space")