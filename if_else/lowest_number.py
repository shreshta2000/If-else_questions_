num=int(input("entre any number"))
num_1=int(input("entre any number"))
num_2=int(input("entre any number"))
if num<num_1 and num<num_2:
	print (num)
elif num_1<num and num_1<num_2:
	print(num_1)
else:
	print(num_2)