import sys

carac = 'di'
minCarac = 12
maxCarac = 16
password = [0 for x in range(0,minCarac)]
passwordAdmin = 'dice'
ended = False

def addInPasswordArray():
	for n in range(1, len(password) + 1):
		if password[len(password) - n] == len(carac) - 1:
			password[len(password) - n] = 0
		else:
			password[len(password) - n] = password[len(password) - n] + 1
			break

def passwordPossibilite():
	data = [carac[n] for n in password]
	return ''.join(data)

def checkIfEnded():
	for n in password: 
		if n != len(carac) - 1: return False
	return True

while True:
	for n in range(0, len(carac)):
		if checkIfEnded():
			if len(password) == maxCarac: 
				ended = True
				break
			else:
				password = [0 for x in range(0, len(password) + 1)]
		if passwordAdmin != passwordPossibilite():
			print('[-] Tried: ' + passwordPossibilite(), end='\r')
			sys.stdout.flush()
		else:
			print('[+] Password Found: ' + passwordPossibilite())
			ended = True
			break
		addInPasswordArray()
	if ended: break