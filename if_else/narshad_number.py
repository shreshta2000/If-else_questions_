number=int(input("entr any number"))
first_number=number//100
last_number=number%10
middle_number=(number-(first_number*100+last_number))/10
if number%(first_number+middle_number+last_number)==0:
	print("it is a harshad number",number)
else:
	print("it is not a harshad number",number)