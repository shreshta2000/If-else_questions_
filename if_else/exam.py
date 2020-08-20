number_of_classes_held=int(input("entre total no of class"))
number_of_classes_attended=int(input("entre how much take class"))
health=input("entre you are well or not")
if number_of_classes_attended/number_of_classes_held*100>=75 and health=="well":
	print("you may give exam")
else:
	print("you may not give exam")