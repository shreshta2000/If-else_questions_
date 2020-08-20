
number=int(input("entre any three digits number"))
first_number=number//100
last_number=number%10
second_number=(number-(first_number*100+last_number))//10
if first_number >= 1 and second_number >= 0 and last_number >= 1:
	print(first_number+second_number+last_number)
else:
	print("invalid! please entre only three digits number")
