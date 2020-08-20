first_angle=int(input("enter first angle of triangle"))
second_angle=int(input("enter second angle of triangle"))
third_angle=int(input("enter third angle of trianlge"))
if first_angle+second_angle+third_angle==180:
	print("it is a triangle")
	if first_angle==90 or second_angle==90 or third_angle==90:
		print("it is right angled traingle")
	if first_angle<90 or second_angle<90 or third_angle<90:
		print("it is acute angled traingle")
	if first_angle>90 or second_angle>90 or third_angle>90:
		print("it is obtuse angled traingle")
else:
	print("it is not a triangle")