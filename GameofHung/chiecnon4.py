# Guess  word

# Import library
import random
import time

# Make function

# Calcul the point of the player
def score(currentPoint,t_value):
	if t_value == 2:
		currentPoint *= 2
	else:
		currentPoint += t_value
	return currentPoint

# Print the point of the player
def currentPoint(cont):
	print("You are having ",cont," points")

# Print the player will or was have points, double points, half of points or lost all points.
def playPoint(coi,tun):
	if non == 10:
		print("You will maybe have double point. You will have maybe "+str(coi*2)+" points.")
	elif non == 11:
		coi /= 2
		print("You was lost a half of your point. You have now "+str(coi)+" points")
	elif non == 12:
		coi = 0
		print("Opps, you was lost all your point. You have now 0 point.")
	elif non == 13:
		turn = tun
		print("Opps, you was lost your turn. It's of the "+ tun +" player.")

# While the player win
def playWin(con,pri):
	print ("Congratulation! You won! You have "+str(con)+" points. The " + pri +" player has "+str(cou)+" points.")

# The time for random.
def t(s):
	time.sleep(s)

# Check if the player input is a letter or not
def check(guess):
	while len(guess)>1 or guess not in 'qwertyuiopasdfghjklzxcvbnm' or guess == "" or blanks.find(guess,0,len(blanks)) != -1:
		# It's string.
		if len(guess)>1:
			print("Guess only a letter in one time.")
		# It's not a letter.
		if guess not in 'qwertyuiopasdfghjklzxcvbnm' or guess == "":
			print("Guess only the letter and no other.")
		# It's has guessed.
		if blanks.find(guess,0,len(blanks)) != -1:
			print("Guess only the letter hasn't guess.")
		guess = input("Guess a letter of the secret word: ")
		return guess
# If the player has a correct guess
def guessCorrect():
	# If the turn is of the first player. 
	if turn == 'first':
		if non<=9:
			non *= 100
			count1 = score(count1,non)
		elif non==10:
			count1 = score(count1,2)
		currentPoint(count1)
	# If the turn is of the second player.
	else:
		if non<=9:
			non *= 100
			count2 = score(count2,non)
		elif non==10:
			count2 = score(count2,2)
		currentPoint(count2)
	m = -1
	# Check the word has x letter's the player haas guessed.
	for fi in range(len(choose)):
		my_guess = choose.find(guess,fi,len(choose))
		if my_guess != -1:
			if my_guess != m:
				m = my_guess
				counter+=1
				blanks=blanks[:m*2] + guess + blanks[m*2+1:]
	print()
	print("Secret word: "+str(blanks))
	# If the player has guessed all.
	if counter == len(choose):
		if turn=='first':
			playWin(count1,"second",count2)
		else:
			playWin(count2,"first",count1)
		return
# If the player has a incorrect guess
def guessIncorrect():
	print("It's wrong!")
	print("You don't have any point.")
	if turn == 'first': # The turn is of the fist player, change the turn for the second player.
		print("It's the turn of the second player.")
		turn = 'second'
	else: # The turn is of the second player, chang the turn for the first player.
		print("It's the turn of the first player.")
		turn = 'first'
	return turn

# Make list of word
Word=['book','ball','door','football','game','buy','dolphin','machine','mouse','heart','lamp','clock','table','key','water','fire','orange','house','horse']
# Random for choose the secret word

def chooseWord():
	choose = random.choice(Word)
	choose = 'football'
	# Random the point for each correct guess.
	non = random.randint(1,13)
	#  Print the point of the player.
	print("Turn of the first player\n")
	print("You are having 0 point")
	print("Turning...")
	t(2)
	# Make the time for count
	counter = 0
	# Point of first player
	count1 = 0
	# Point of second player
	count2 = 0
	# Set a turn
	turn = 'first'
	if non<=9:
		# If the player has a correct answer, he will have current points + non
		print("You will maybe have "+str(non*100)+" points")
	elif non==13:
		non = 0
		# If non == 13, the player was lost his turn.
		turn='second'
		print("Opps, you was lost your turn.")
	else:
		# If non == 10(<=> current point * 2 <=> 0 * 2 == 0), non == 11(<=> current point /2 <=> 0 / 2 == 0), non == 12(<=> current point == 0) so not thing change.
		print("Not thing change.")
		non = 0
	return choose

# The blank '_ _ _ _ _ ' of the secret word
def my_Blanks():
	# The length of the secret word
	blanks='_ '*len(choose)
	print("Secret word: "+str(blanks))
	return blanks

# Guess a letter
def secretGuess():
	#Guess the letter
	guess = input("Guess the letter of the secret word: ")
	return guess

# Starting program

playAgain = 'yes'
while playAgain == 'yes':
	
	# Use function
	choose = chooseWord()
	blanks = my_Blanks()
	guess = secretGuess()
	
	# Make a loop infinity
	while 0 != 1:
		
		guess = check(guess)
		
		# If the player has a correct guess.
		if guess in choose:
			guessCorrect()
		
		# If the player has incorrect guess.
		else:
			guessIncorrect()
		
		# Quay chiếc nón
		non = random.randint(1,9)
		# The turn is of the first player
		
		if turn == 'first':
			currentPoint(count1)
		
		# The turn is of the second player
		else:
			currentPoint(count2)
		
		print("Turning...")
		t(2)
		
		if non <= 9:
			print("You will maybe have "+str(non*100)+" points")
		
		elif turn == 'first':
			count1 = playPoint(count1,'second')
		
		elif turn == 'second':
			count2 = playPoint(count2,'first')
		
		guess = secretGuess()

	# Ask the player if he want to play again or not.
	playAgain = input("Play again? (yes or no): ")
