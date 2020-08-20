# i = 0
# while i <= 50:
#   if i != 0:
#     print(i)
#   i = i + 5
# a = -1
# while a >= (-10):
# 	print (-a)
# 	a = a -1



# char_list = ["a","n","t","a","t","n","n","a","x","u","g","a","x","a"]
# i = 0
# a = []
# while i < len(char_list):
# 	if char_list[i] not in a:
# 		a.append (char_list[i])
# 	i = i + 1
# print(a)
	
# j = 0
# b = [ ]
# while j<len(a):
# 	k = 0
# 	count = 0
# 	c=[ ]
# 	while k<len(char_list):
# 		if a[j] == char_list[k]:
# 			count = count + 1
# 		k +=1
# 	c.append(a[j])
# 	c.append(count)
# 	b.append(c)
# 	j = j + 1
# print(b)


# kitna_paisa_hai = [3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
# i = 0
# croropathi = 0
# lakhpathi = 0
# dilwale = 0
# while i<len(kitna_paisa_hai):
# 	if kitna_paisa_hai[i] > 10000000:
# 		croropathi = croropathi + 1
# 	elif kitna_paisa_hai[i] > 100000:
# 		lakhpathi = lakhpathi + 1
# 	else:
# 		dilwale = dilwale + 1
# 	i  = i + 1
# print("croropathi",croropathi)
# print("lakhpathi",lakhpathi)
# print("dilwale",dilwale)


# duplicates = [19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# i = 0
# a = []
# while i<len(duplicates):
# 	j = i + 1
# 	while j<len(duplicates):
# 		if duplicates[i] == duplicates[j]:
# 			b = duplicates[i]
# 			a.append(b)
# 			break
# 		j = j + 1
# 	i = i + 1
# print(a)


# list1 = [1,45,50,16,19,23,92,90,56]
# i = 0
# length = 0
# while i<=len(list1):
# 	length = length + 1
# 	i = i + 1
# print(length)


# questions_list = ["what is the capital of india","how many continents are there","ng mai kaun course padhaya jaata hai"]
# options_list = [["chandhgarh","bhopal","chennai","delhi"],["four","seven","nine","eight"],["software","counseling","tourism","agriculture"]]
# answer_list = [4,2,1]
# i = 0
# while i<len(questions_list):
# 	print(questions_list[i])
# 	j = 0
# 	while j<=len(options_list):
# 		print(options_list[i][j])
# 		j = j + 1
# 	value = int(input("enter your num"))
# 	if value == answer_list[i]:
# 		print("your answer correct")
# 	else:
# 		print("your answer wrong")
# 		break
# 	i = i + 1





# questions_list = ["what is the capital of india","how many continents are there","ng mai kaun course padhaya jaata hai"]
# options_list = [["chandhgarh","bhopal","delhi","goa"],["four","seven","nine","eight"],["software","counseling","tourism","agricu"]]
# answer_list = ["delhi","seven","software"]
# i = 0
# while i<len(questions_list):
# 	print(questions_list[i])
# 	j = 0
# 	while j<len(options_list[i]):
# 		print(options_list[i][j])
# 		a = options_list[i][j]
# 		b = answer_list[i]
# 		j=j+1
# 	lifeline = int(input("enter your num"))
# 	if lifeline == 5050:
# 		print(a)
# 		print(b)
# 		lifeline = input("enter your answer")
# 	if lifeline in answer_list:
# 		print("your answer right")
# 	else:
# 		print("your answer is wrong")
# 		break
# i=i+1


# bubble_sort = [-2,45,0,11,-9]
# i=0
# while i<len(bubble_sort):
# 	j=i+1
# 	while j<len(bubble_sort):
# 		if bubble_sort[i]>bubble_sort[j]:
# 			swap = bubble_sort[i]
# 			bubble_sort[i] = bubble_sort[j]
# 			bubble_sort[j] = swap
# 		j=j+1
# 	i=i+1
# print(bubble_sort)


# marks = [10, 32, 42, 65, 67, 89, 76, 38, 67]
# total_marks = 0
# counter = 0
# while counter < len(marks):
# 	total_marks = total_marks + marks[counter]
# 	counter = counter + 1
# print(total_marks)


# name = ["savitri","phule","26"]
# i = 0
# while i<len(name):
# 	print(name[i])
# 	i=i+1

# a=[]
# a=[2,4,8,10,15]
# if len(a) == 0:
# 	print("empty list",a)
# else:
# 	print("not empty list",a)


# # write a program to replace the last element in list with another list
# list1 = [1,3,5,7,9,10]
# list2 = [2,4,6,8]
# list1.remove(10)
# list2.remove(8)
# print(list1)
# print(list2)
# list3 = list1 + list2
# print(list3)
  


# def ask_questions():
# 	print ("who is the founder of facebook")
# 	print ("mark zuckerberg")
# 	print ("bill gates")
# 	print ("steve jobs")
# 	print ("larry page")
# i=1
# while i<=5:
# 	print (ask_questions(),i)
# 	i=i+1


# i=1
# while i<=100:
# 	print(ask_questions(),i)
# 	i=i+1  

# numbers = [3,5,7,34,2,89,2,5]
# i=0
# maxi = 0
# while i<len(numbers):
# 	if numbers[i]>maxi:
# 		maxi = numbers[i]
# 	i=i+1
# print(maxi)

# numbers = [1,2,3,4,5]
# i=0
# sum=0
# while i<len(numbers):
# 	sum = sum + numbers[i]
# 	i=i+1
# print(sum)

# unorder_list = [6,8,4,3,9,56,0,34,7,15]
# i=0
# while i<len(unorder_list):
# 	j=0
# 	while j<len(unorder_list):
# 		if unorder_list[i]<unorder_list[j]:
# 			sort = unorder_list[i]
# 			unorder_list[i] = unorder_list[j]
# 			unorder_list[j] = sort
# 		j=j+1
# 	i=i+1
# print(unorder_list)

# reverse_list = ["z","A","A","B","E","M","A","R","D"]
# a=len(reverse_list)-1
# while a>=0:
# 	print(reverse_list[a])
# 	a=a-1


# list1 = [8,6,4,8,4,50,2,7]
# i=0
# mini=list1[0]
# while i<len(list1):
# 	if list1[i]<mini:
# 		mini = list1[i]
# 	i=i+1
# print(mini)


# def sum():
# 	print(12+13)
# sum()ss

# def welcome():
# 	print("welcome to function")
# welcome()

# def iseven():
# 	if (12%2==0):
# 		print("even")
# 	else:
# 		print("odd")
# iseven()

# def great(*names):
# 	for name in names:
# 		print("welcome",name)
# great("rinki","vishal","kartik","bijendra")
# great()

# def info(name,age = "20"):
# 	print(name  +  "is"  +  age  +  "years old")
# info("sonu")
# info("sana", "17")
# info("umesh", "18")


# def studentsdetails(name,currentmilestone,mentor):
# 	print("Hello" , name , "yours" , currentmilestone , "concept" , "is clear with the help of" , mentor)
# studentsdetails("nilam","loop","evanjaline")


# def function_print_lines(name,current):
# 	print("my name is",name)
# 	print("I am the founder of",current)
# function_print_lines("rishadh","navgurukul")

# def students_names(*name):
# 	for i in name:
# 		print(i)
# students_names("evanjaline","joys","ankitha")


# def isgreaterthan20(num1,num=20):
# 	print(num1,num)
# isgreaterthan20(12)

  
# def add_numbers(num1,num2):
# 	print(num1+num2)
# add_numbers(56,12)

# def add_numbers_list(num1,num2):
# 	i=0
# 	a=[]
# 	while i<len(num1):
# 		sum=num1[i]+num2[i]
# 		a.append(sum)
# 		i=i+1
# 	for i in a:
# 		print(i)
# add_numbers_list([50,60,10],[10,20,13])


# def check_numbers(num1,num2):
# 	if num1%2==0 and num2%2==0:
# 		print(num1,num2,"both are even")
# 	else:
# 		print(num1,num2,"both are not even")
# check_numbers(24,19)


# def check_numbers_list(num1,num2):
# 	i=0
# 	while i<len(num1):
# 		if num1[i]%2==0 and num2[i]%2==0:
# 			print(num1[i],num2[i],"both are even")
# 		else:
# 			print(num1[i],num2[i],"both are not even")
# 		i=i+1
# check_numbers_list([2,6,18,10,3,75],[6,19,24,12,3,87])


# def calculator(num_x,num_y,operation):
# 	if operation == "+":
# 		return num_x + num_y
# 	elif operation == "-":
# 		return num_x - num_y
# 	elif operation == "*":
# 		return num_x * num_y
# 	elif operation == "//":
# 		return num_x // num_y
# 	else:
# 		return num_x / num_y
# values = calculator(10,15,"+")
# print(values)



# def calculator(num_x,num_y,operation):
# 	if operation == "+":
# 		add_result = num_x+num_y
# 		return add_result
# 	elif operation == "-":
# 		subtract_result = num_x-num_y
# 		return subtract_result
# 	elif operation == "*":
# 		multiple_result = num_x*num_y
# 		return multiple_result
# 	elif operation == "//":
# 		divide_result = num_x//num_y
# 		return divide_result
# num_x = int(input("enter num_x"))
# num_y = int(input("enter num_y"))
# operation = input("enter your operation")
# print(calculator(num_x,num_y,operation))
# print(calculator(add_result)
# printcalculator(subtract_result)
# calculator(multiple_result)
# calculator(divide_result)


# places = ["delhi","gujurath","rajasthan","kerala"]
# i=len(places)-1
# while i>=0:
# 	print(places[i])
# 	i=i-1
# a=3)
# b=9
# print(a//b
# name="_shreshta"
# length=len(name)
# # print(length)


# rev=0
# num=int(input("enter your number"))
# # rev=0
# while num>0:
# 	rem=num%10
# 	rev=rev*10+rem
# 	num=num//10
# print(rev)


# age=int(input("enter your age:"))
# sex=input("enter your sex:")
# marital_status=input("enter your marital status:")
# if age>20:
#   print("eligible for working")
#   if sex=="female":
#     print("have to work in urban area")
#   elif sex=="male" and age<40:
#     print("can work in either urban or rural area")
#   elif sex=="male" and age>40 and age<60:
#     print("have to work in urban area")
#   else:
#     print("invalid information")
# else:
#   print("ERROR")



# 


# # param1=1 ,param2=2
# def add(param1, param2):
# 	add4=param1+param2
# 	return add4
# print(add(7,6))

# def mul(a,b):
# 	mul=a*b
# 	return mul
# print(mul(3,4))


# def div(a,b):
# 	div=a/b
# 	return div
# print(div(4,2))


# year=int(input("enter your year"))
# if year//100!=0:
# 	print(year//100+1,"century") 
# elif year<=1 or year<=100:
# 	print("1st century")
 
# if year%100==0:
# 	print(year//100)
# else:
#  	print(year//100+1)



# c=0
# d=1
# while c<3:
# 	print ("loop ke andar",c,d)
# else:
# 	print ("loop ke bahar" ,c,d)

# n = 6
# s = 0
# i = 1

# while i <= n:
#     s = s + i
#     i = i + 1

# print (s)

# num=int(input("enter any number"))
# i = 2
# while (i<num):
#     if (num%i == 0):
#         print(num, 'is not a prime number')
#         break
#     i = i + 1
# else:
#     print(num, 'is a prime number')


# # i = 0
# while(i<5):
#     j = 0
#     while(j<5): #loop2
#         if (j > 3): 
#             break 
#         else:
#             print "*", 
#         j = j + 1    
#     print ('')
#     i = i +

# sum=0
# i = 1
# while(i <= 140):
#     if(i % 3 == 0):
#     	print(i)
#     	# sum = sum+i
#     	i = i - 1


# i=1
# while i<=140:
# 	if i%3==0:
# 		print(i)
# 	i=i+1
# i=0
# while(i<10):
# 	j = 0
# 	while(j<=5):
# 		print(j)
# 		j = j + 1
# 		i = i + 1


# i = 0
# num = int(input("Enter your number:- "))
# while(i <= num):
# 	if(num > 0):
# 		print("it is positive")
# 		break
# 	elif(num < 0):
# 		print("it is negetive")
# 		break
# 	else :
# 		print("zero")
# 	i = i + 1
# name="pencil"
# for x in range (6):
# 	print(x)

# x = "wowo"
# w = "" 
# for i in x: 
#     w = i + w 
#     if (x==w): 
#         print("Yes, it is palidrome",w)
#     else:
#     	print ("not palindrome")

        
# name="shreshta" 
# lenght=len(name)
# lenght_1=lenght%2
# i=1
# while i<=lenght:
#  	if lenght_1==0:
#  		print(lenght_1)

# i=159
# while i>149:
# 	z=i-149
# 	print(z)
# 	i=i-1
# password=input("enter the num,special,alphabet=")
# if password>='0' or password<='9':
# 	if password>='A' or password<='Z' and password>='a' or password<='z':
# 		if '@' in password  and len(password)==8:
# 			print("password is good")
# 		else:
# 			print("password is not good")
# 	else:
# 		print("nothing")
# else:
# 	print("not good")		































