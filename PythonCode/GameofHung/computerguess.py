# Geuss word
# Import library
import random
import copy
# Set
# counter of the correct character of secret word
counter = 0
playAgain = 'yes'
# Set blanks for secret word
blanks = '_ '
secret = 0
hasgot = 'False'
# Open file
list = open("data.txt","r")
# Read file	
lis = list.read()
# change all charater to normal mode
lis = lis.lower()
# remove all special cahrater
lis = lis.replace("."," ")
lis = lis.replace(","," ")
# remove the \n in the text
lis = lis.replace("\n"," ")
# make a list of all charater of the text
mylist = lis.split(" ")
# make another list
dif = copy.copy(mylist)
# Make function
def openfile():
	# Global
	global dif, mylist, lis
	# search numbers and remove it
	for q in range(10):
		# make the number to a string
		q = str(q)
		# if list has a number, remove
		if lis.find(q) != -1:
			# remove
			lis = lis.replace(q," ")
	# Say the player search a word for the secret word
	print("Read this text and search a secret word:\n"+str(lis))
	# Search the same word in list
	for a in range(len(mylist)):# take an element of the list and compare with other
		for b in range(a):# compare with a
			# if it has two same element
			if mylist[a] == mylist[b]:
				# remove one
				dif.remove(mylist[a])
				# stop this loop for take another element a
				break
	# it has  a empty element of the end so i must remove it
	dif.remove(dif[len(dif) - 1])
	# close file
	list.close()
	# just return
	return dif
# Set a list
chooseLette = []
# continue make functions
def ChooseWord():
	# global
	global chooseWord,s,chooseLette
	for c in range(len(dif)):
		# search words has the numbers of of the letters == the one of the player input
		if len(dif[c]) == secret:
			# add that word in a list
			chooseLette.append(dif[c])
	# choose a word
	chooseWord = random.choice(chooseLette)	
# this function is for choose a letter of the word has choosed
def ChooseLetter():
	#global
	global chooseWord,s
	#choose the position of the letter
	s = random.randint(0,len(chooseWord)-1)
	# choose letter
	chooseLetter = chooseWord[s]
	# i don't know how to remove a charater of a word so i use replace(letter," ") so when it random the space it must to 'rerandom'
	while chooseLetter == " ":
		# 'rerandom' position of the letter
		s = random.randint(0,len(chooseWord)-1)
		# choose letter
		chooseLetter = chooseWord[s]
	# return
	return chooseLetter
# just notice for the under function
iden = 'yes'
# If corrected guess
def guessCorrect():
	# global
	global blanks,iden,counter,chooseword,chooseWord
	# counter of the number of repeat character
	counter2 = 0
	a = -1
	m = -1
	c = 0
	b = -1
	# ask the player of the position of the letter
	inde = input("Enter the position of this letter in the word: ")
	while not inde.isdigit():
		inde = input("Enter the position of this letter in the word: ")
	# if there more than one letter so i make a list of the position of letters
	ind = inde.split(";")
	# count how many total cahrater the computer has guess
	counter += len(ind)
	for nbletter in range(secret): 
		# if it has more same charater in the secret word
		if counter2 < len(ind):
			a = a + 1
		else:
			break
		# to verifier if this letter has found or not
		if ind[a] != m:
			# save to know this letter has found 
			m = ind[a]
			# count the the number of repeat charater
			counter2 += 1
			# set the the element to a number
			ind[a] = int(ind[a])
			#change blanks with show letters has guessed
			blanks = blanks[:ind[a] * 2] + chooseLetter + blanks[ind[a] * 2 + 1:]
	#show blanks
	print(str(blanks))
	for x in range(len(chooseLette)):
		print(x)
		print(len(chooseLette))
		if x >= len(chooseLette) - 1:
			break
		if chooseLette[x].find(chooseLetter) != ind[0]:
			chooseLette.remove(chooseLette[x])
	while chooseword.find(chooseLetter) != ind[0]:
		chooseWord = random.choice(chooseLette)
		chooseword = chooseWord
	for x in range(len(chooseLette)):
		if x >= len(chooseLette) - 1:
			break
		if chooseLetter not in chooseLette[x]:
			chooseLette.remove(chooseLette[x])
	# return
	return secret
# Start program
# open file data.txt
dif = openfile()
# ask the player the nubmer of the secret word
secret = int(input("Enter the number of the secret word: "))
# make blanks of the secret word
blanks = '_ ' * secret
# choose word
ChooseWord()
chooseword = chooseWord
# choose letter
chooseLetter = ChooseLetter()
print(str(chooseLette))
while playAgain == 'yes':
	answer = None
	# Make a loop infinity
	while blanks.find("_") != -1:
		# ask the player the letter's computer has guessed is correct or not
		while (answer != 'y' or answer != 'n'):
			answer = input("Is '"+str(chooseLetter)+"' a letter in the secret word? (y or n) ")
			if answer == 'y':
				break
			if answer == 'n':
				break
		# if it is corect
		if answer == 'y':
			secret = guessCorrect()
			# remove letter it has guessed
			chooseWord = chooseWord.replace(chooseLetter," ")
			# if computer has guessed all
			if counter == secret:
				print("YES! I won! HAHAHAHAHAHA.....")
				break
		# if the answer of the player is no
		else:
			# remove the word's computer has choosed
			chooseLette.remove(chooseword)
			for word in range(len(chooseLette)):# remove all word has the chooseLetter
				if len(chooseLette) <= word:
					if chooseLetter in chooseLette[len(chooseLette) - 1]:
						chooseLette.remove(chooseLette[len(chooseLette) - 1])
					break
				if chooseLetter in chooseLette[word]:
					chooseLette.remove(chooseLette[word])
			chooseWord = random.choice(chooseLette)
			chooseword = chooseWord
		# choose letter
		chooseLetter = ChooseLetter()
		while chooseLetter in blanks:# if it 
			chooseLetter = ChooseLetter()
	# ask the player want to play again or not
	playAgain = input("Do you want to play again? (yes or no) ")
	# if the player want to play again
	if playAgain == 'yes':
		# Set
		# counter of the correct character of secret word
		counter = 0
		playAgain = 'yes'
		blanks = '_ '
		secret = 0
		hasgot = 'False'
		# open file
		list = open("data.txt","r")
		# read file
		lis = list.read()
		# make all charater to the normal mode
		lis = lis.lower()
		# no charater spacial
		lis = lis.replace("."," ")
		lis = lis.replace(","," ")
		lis = lis.replace("\n"," ")
		# make a list of the word's text
		mylist = lis.split(" ")
		# make another list same the last one
		dif = copy.copy(mylist)
		# open file
		dif = openfile()		
		# ask the number of the secret word
		secret = int(input("Enter the number of the secret word: "))
		# set blanks's secret word
		blanks = '_ ' * secret
		# choose word
		ChooseWord()
		# chooseletter
		chooseLetter = ChooseLetter()

