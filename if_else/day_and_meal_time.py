day=input("entre day monday or tuesday")
meal_time=input("entre any meal time")
if day =="monday":
	if meal_time=="breakfast":
		print("poori sabzi")
	elif meal_time=="lunch":
		print("sambhar rice")
	elif meal_time =="dinner":
		print("chicken rice")
elif day =="tuesday":
	if meal_time =="breakfast":
		print("poha")
	elif meal_time =="lunch":
		print("rajma rice")
	elif meal_time =="dinner":
		print("roti sabzi")
else:
	print("invalid! please entre day monday or tuesday")