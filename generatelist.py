import sys

# Characters that will be part of every possible password
carac = input('Characters list (You can skip this one) [Example: abcdefABCDEF"#$"!]: ')
carac = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&/()=?*' if len(carac.strip()) == 0 else carac
# Minimum characters
minCarac = input('Minimum characters: ')
minCarac = 6 if len(minCarac) == 0 else int(minCarac)
# Maximum characters
maxCarac = input('Maximum characters (Default: 8): ')
maxCarac = 8 if len(maxCarac) == 0 else int(maxCarac)
# Password array where all the numbers that will later turn to letters are stored
password = [0 for x in range(0,minCarac)]
# A simple variable to stop the While Loop
ended = False
# This is the variable that stores the name of the file
fileName = input('File name (Default: wordlist): ')
fileName = 'wordlist.txt' if len(fileName.strip()) == 0 else fileName + '.txt'
# Opens the file in write mode
file = open(fileName, 'w')
pCount = 0

def addInPasswordArray():
	for n in range(1, len(password) + 1):
		if password[len(password) - n] == len(carac) - 1:
			password[len(password) - n] = 0
		else:
			password[len(password) - n] = password[len(password) - n] + 1
			break

# Changes the numbers in the password array to numbers and returns a string
# Example: [0,0,0,1,3] -> aaabd
def passwordPossibilite():
	data = [carac[n] for n in password]
	return ''.join(data)

# Checks if all the possibilites ended
def checkIfEnded():
	# Loops the password array...
	for n in password: 
		# ...and checks if the password element isn't equal to the last character possible
		if n != len(carac) - 1: return False
	# Returns True if it ended
	return True
	
print('\n')
while True:
	# Loops the characters
	for n in range(0, len(carac)):
		# Checks if all the possibilites ended in the respective characters length
		if checkIfEnded():
			# If the possibilites ended and the length of the password array its equals to the maximum characters break the loop
			if len(password) == maxCarac: 
				ended = True
				break
			else:
				password = [0 for x in range(0, len(password) + 1)]
		# Writes the password possibilite in the file
		file.write(passwordPossibilite() + '\n')
		addInPasswordArray()
		pCount += 1
		print('Generated {} possibilites'.format(pCount), end='\r')
		sys.stdout.flush()
	# Stops the while loop if all ended
	if ended: break