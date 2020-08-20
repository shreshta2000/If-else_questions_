kitchen_team=input("entre any team")
kitchen_team_health=input("entre team well or not well")
if kitchen_team_health=="well":
	if kitchen_team=="a":
		print("kitchen_team a have to make food")
		if kitchen_team=="b":
			print("kitchen_team b have to make food")
			if kitchen_team=="c":
				print("kitchen_team c have to make food")
elif kitchen_team_health=="not well":
	if kitchen_team=="a":
		print("kitchen team b have to make food")
		if kitchen_team=="b":
			print("kitchen team c have to make food")
			if kitchen_team=="c":
				print("kitchen team a have to make food")
else:
	print("invalid! please entre kitchen_team a or b or c and kitchen_team_health is well or not well")