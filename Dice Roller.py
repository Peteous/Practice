import random

# If compiling in Terminal, inputs must be entered within quotes, or errors will occur

# Define function of dice roll, which generates a value as though a dice of diceSides sides was rolled
def roll(diceSides):
	diceSides = int(diceSides)
	result = random.randint(1,diceSides)
	return result

# Define initial loop condition as true so loop happens
cont = True

# Script loop so dice rolling can continue until you're satisfied
while(cont == True):
	# Get dice input from the user, with input specified, and cast as a list
	diceToRoll = input('What would you like to roll? \n(Example Format 1d6, 2d4, etc)\n')
		#Note: when compiling via Terminal, dice input must be typed in quotes ''
	diceToRoll = list(diceToRoll)

	# Determine the length of the diceToRoll list for proper for loop iteration
	inputStringLength = len(diceToRoll)

	# Define dNumber and dSides list to avoid errors
	dNumber = ['0']
	dSides = ['0']
	for i in range(0,inputStringLength):
		if not i == 0:
			dNumber.append('0')
			dSides.append('0')

	# Set diceNumber such that first if statement will be true until the 'd' character is found
	diceNumber = -1

	# Iterate through the list to find 3 groups of characters: 1st, number of dice being rolled, 2nd,
	# that dice are being rolled, 3rd, how many sides do the dice have
	for index in range(0,inputStringLength):
		if not diceToRoll[index] == 'd' and diceNumber == -1:
			dNumber[index] = int(diceToRoll[index])
		elif diceToRoll[index] == 'd':
			diceNumber = 0
			d = index
		elif not diceToRoll[index] == 'd' and diceNumber == 0:
			dSides[index] = int(diceToRoll[index])

	# Get rid of excess values in dNumber
	for k in range(0,inputStringLength):
		if k >= d:
			dNumber.remove(dNumber[inputStringLength-1])
			inputStringLength -= 1
			k-=1

	# Get rid of excess values in dSides
	for j in range(0,inputStringLength):
		if j <= d:
			dSides.remove(dSides[0])
			inputStringLength -= 1
			j-=1

	# Cast diceToRoll as an int, since the number of dice to be rolled is an int
	numString = ''
	diceToRoll = None
	for x in dNumber:
		if numString == '':
			numString = str(dNumber[dNumber.index(x)])
		else:
			numString += str(dNumber[dNumber.index(x)])
	diceToRoll = int(numString)

	# Cast diceSides as an int, since dice have an int number of sides
	sidString = None
	for y in dSides:
		if sidString == None:
			sidString = dSides[dSides.index(y)]
		else:
			sidString += str(dSides[dSides.index(y)])
	diceSides = int(sidString)

	# Use the roll function for every number of die that there is, adding the value together to Roll
	Roll = None
	for index1 in range(diceToRoll):
		if Roll == None:
			Roll = roll(diceSides)
		else:
			Roll += roll(diceSides)

	# Output the value of the roll, and ask the user if they want to roll again
	print('\nYou rolled ' + str(diceToRoll) + ' ' + str(diceSides)+ '-sided dice' + '\nAnd your result is: ' + str(Roll))
	again = input('\nWould you like to roll again?\n(Respond Yes or No)')

	# Determine if the user wants to continue or not, and loop or break accordingly
	if (again == 'Yes' or again == 'yes' or again == 'y' or again == 'Y'):
		print('\n')
		cont = True
		continue
	elif (again == 'No' or again == 'no' or again == 'n' or again == 'N'):
		print('\nThank you for playing\n\nProgram terminated')
		cont = False
		continue
	else:
		print('\nI\'m sorry, I didn\'t understand that.\n\nProgram terminated')
		cont = False
		continue
