import random
print("Welcome to the guessing game:")
print("Please choose your level:")

#Your level
print("press 1.Beginner(0-100)    press 2.Semi-Pro(0-1000)   press 3.Pro(0-10000)    4.Other ")

level=input()
level=int(level)
if level==1:
	print("So your level is beginner.")
	print("Well, the secret number is between 0 and 100.")
	x=random.randint(0,100)
	print("Input the max time for guess: ")
	time=input()
	time=int(time)
	print("Guess the secret number:")
	secret=input()
	secret=int(secret)
	counter=1
	while secret!=x:
		print("It's false. False "+str(counter)+" time(s)")
		if counter>=time:
			print("GAME OVER. The secret number is "+str(x))
			break
		counter=counter+1
		if x>=secret:
			print("The secret number is bigger than "+ str(secret))
		else:
			print("The secret number is smaller than "+str(secret))
		print("So, try again:")
		secret=input()
		secret=int(secret)
	if secret==x:
		print("Congratulation. You have my number after "+str(counter)+" times")
elif level==2:
	print("So your level is semi-pro.")
	print("Well, the secret number is between 0 and 1000")
	x=random.randint(0,1000)
	print("Input the max time for guess:")
	time=input()
	time=int(time)
	print("Guess the secret number:")
	secret=input()
	secret=int(secret)
	counter=1
	while secret!=x:
		print("It's false. False "+str(counter)+" time(s)")
		if counter>=time:
			print("GAME OVER")
			break
		counter=counter+1
		if x>=secret:
			print("The secret number is bigger than "+str(secret))
		else:
			print("The secret number is smaller than "+str(secret))
		print("So, try again:")
		secret=input()
		secret=int(secret)
	if secret==x:
		print("Congratulation. You have my number after "+str(counter)+" times")
elif level==3:
	print("So your level is pro.")
	print("Well, the secret number is between 0 and 10000.")
	x=random.randint(0,10000)
	print("Input the max time for guess: ")
	time=input()
	time=int(time)
	print("Guess the secret number:")
	secret=input()
	secret=int(secret)
	counter=1
	while secret!=x:
		print("It's false, False "+str(counter)+" time(s)")
		if counter>=time:
			print("GAME OVER.")
			break
		counter=counter+1
		if x>=secret:
			print("The secret number is bigger than "+str(secret))
		else:
			print("The secret number is smaller than "+str(secret))
		print("Please try again:")
		secret=input()
		secret=int(secret)
	if secret==x:
		print("Congratulation. You have my number after "+str(counter)+" times")
elif level==4:
	print("Well, choose the minium number and the maxium number:")
	print("The minium number:")
	min=input()
	min=int(min)
	print("The maxium number:")
	max=input()
	max=int(max)
	print("So, the secret number is between "+str(min)+" and "+str(max))
	x=random.randint(min,max)
	print("Input the max time for guess:")
	time=input()
	time=int(time)
	print("Guess the number:")
	secret=input()
	secret=int(secret)
	counter=1
	while secret!=x:
		print("It's false. False "+str(counter)+" time(s)")
		if counter>=time:
			print("GAME OVER. The secret number is "+str(x))
			break
		counter=counter+1
		if x>=secret:
			print("The secret number is bigger than "+str(secret))
		else:
			print("The secret number is smaller than "+str(secret))
		print("Try again:")
		secret=input()
		secret=int(secret)
	if secret==x:
		print("Congratulation. You have my nuber after guessing "+str(counter)+" times")
else:
	print("ERROR")
