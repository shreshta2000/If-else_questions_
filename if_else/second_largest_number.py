number=int(input("entre any number"))
number_1=int(input("entre another number"))
number_2=int(input("entre another number"))
if number<number_1 and number_1<number_2:
	print(number_1)
elif number>number_1 and number<number_2:
	print(number_1)
else:
	print(number_2)