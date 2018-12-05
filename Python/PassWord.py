passwordFile = open('SecretPassword.txt')
secretPassword = passwordFile.read()
print('Enter your Password.')
typedPassword = input()
if typedPassword == secretPassword :
	print('Access Granted')
	if typedPassword == '12345' :
		print('That password is one that an idiot puts on their luggage.')
else :
	print('Access denied.')