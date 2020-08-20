age=int(input("entre your age"))
sex=input("entre your gender")
marital_status=input("entre you are married or unmarried")
if sex=="female":
	print("she will work in urban areas")
if sex=="male":
	if age>=20 and age<=40:
		print("he may work anywhere")
	elif age>40 and age <=60:
		print("he will work in urban areas")
	else:
		print("error")