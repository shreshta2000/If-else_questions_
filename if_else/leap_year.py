year=int(input("entre any year"))
if year%4==0 and year%100!=0 and year%400!=0:
	print("it is leap year",year)
else:
	print("it is not leap year")