import time
def t(s):
	for x in range(s):
		print(".",end="",flush=True)
		time.sleep(1)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("\t\t\b\b-------------------------------|----------|----------------------------")
print("\t\t\b\b-------------------------------|DEATH NOTE|----------------------------")
print("\t\t\b\b-------------------------------|----------|----------------------------")
t(4)
print("")
print("\n\t\t\b\bThis note can kill a human.          press enter to continue")
enter=input()
if enter=='':
	print("\n\t\t\b\bThe human whose name in wrtten in this note will die")
	print("")
	t(5)
	print("\n\t\t\b\bThis note will not take effet unleas the writer has person's face in their mind his/her name...")
	print("")
	t(5)
	print("\nIf the cause of death is not specified, the person will simply die of a heart attack. And the person will die in 40 seconds.")
	print("")
	t(5)
	print("\n\t\t\b\bAfter writting the cause of death, details of the death should be written next 400 seconds...")
	t(2)
	print("")
	print("\t\t\t\t\b\b\bTHE END")
	t(2)
	print("")
	print("\t\tSee you later. Thanks you for listen ")
