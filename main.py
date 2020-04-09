import sys

# Constant Variables (can be changed manually before startup)
CARAC = '1234567890'
MIN_CARAC = 1
MAX_CARAC = 6
FILENAME = 'wordlist.txt'

password = [0 for x in range(0, MIN_CARAC)]
file = open(FILENAME, 'w')
current_password_count = 0
max_possibilities = sum([len(CARAC) ** current_carac for current_carac in range(MIN_CARAC, MAX_CARAC + 1)])

def increment_password_combination():
	for n in range(1, len(password) + 1):
		if password[len(password) - n] == len(CARAC) - 1:
			password[len(password) - n] = 0
		else:
			password[len(password) - n] = password[len(password) - n] + 1
			break

# Changes the numbers in the password array to numbers and returns a string
# Example: [0,0,0,1,3] -> aaabd
def generate_password_possibility():
	data = [CARAC[n] for n in password]
	return ''.join(data)

# Checks if all the possibilites ended
def has_ended():
	# Returns True if the "password" array sum equals to the length of the "CARAC" array minus 1 multiplying by the len of the "password" array...
	# ...which means this actually checks if the "password" array has reached it's final result
	# Example: if you configured the "CARAC" array to be 'ABC' the final result should be 'CCC', which means, that the "password" array would be [2,2,2]...
	# ...therefore, the sum of the "password" array would be 6...
	# ...and the multiplication result would be 6 as well because the length of the "CARAC" array minus 1 should be 2 and the length of the "password" array should be 3
	return sum(password) == (len(CARAC) - 1) * len(password)
	
while True:
	# Loops the characters
	# Writes the password possibilite in the file
	password_possibility = generate_password_possibility()
	file.write(password_possibility + '\n')
	current_password_count += 1
	
	print('Generated {}/{} possibilites. Current: {}'.format(current_password_count, max_possibilities, password_possibility), end='\r')
	sys.stdout.flush()
	if has_ended():
		# If the possibilites ended and the length of the password array its equals to the maximum characters break the loop
		if len(password) == MAX_CARAC: 
			break
		# Else, increases the password range limit
		else:
			password = [0 for x in range(0, len(password) + 1)]
	else:
		increment_password_combination()