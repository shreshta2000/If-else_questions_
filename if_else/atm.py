print("enter your card")
language=input("select your language hindi or english: ")
if language=="hindi" or language=="english":
	print("you select language",language)
	pin=int(input("enter your pin: "))
	if pin==2345:
		account_type=input("enter your account type current or savings or credit: ")
		if account_type=="savings" or account_type=="current" or account_type=="credit":
			print("your account type is",account_type)
		purpose=input("enter the purpose you enter card balance inquariy or transfer or withdrawal: ")
		if purpose=="withdrawal":
			amount=int(input("enter how much you want cash: "))
			if amount>=100 and amount<=10000:
				print("please collect your cash")
				receipt=input("enter you want print receipt yes or no: ")
				if receipt=="yes":
					print("you have balance",15000-amount)
			else:
				print("you don't have money that much")
		elif purpose=="balance inquariy":
			print("you have 15000")
		elif purpose=="transfer":
			account_number=int(input("enter whoes account number you want transfer money"))
			if account_number==123456789:
				ifsc_code=input("enter his/her ifsc code")
				if ifsc_code==sbi1234:
					amount=int(input("enter how much you to transfer money"))
					if amount<=15000:
						print("amount transfer",amount)
						recipit=intput("enter you want print recipit yes or no")
						if recipit=="yes":
							print("you have balance",15000-amount)
					else:
						print("you have only 15000")
				else:
					print("invalid! ifsc code")
			else:
				print("wrong! account number")
		else:
			print("wrong!purpose you chosse")
	else:
		print("wrong! password")
else:
	print("invalid!language")
print("collect your card")
print("thanks!for using sbi atm")

