number=int(input("entre any any two digits number"))
reminder=number%10
quotient=number//10
reverse_number=reminder*10+quotient
if reverse_number!=0:
	print(reverse_number)
else:
	print("invalid!please entre any two digits number")