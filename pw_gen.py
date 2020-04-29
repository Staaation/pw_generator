#! python3
# pw_gen.py


import sys, random, os
os.chdir('.\\quizDirectory')
if len(sys.argv) < 4:
	print('\nA password will be generated for you, please follow these instructions \n' +
	'Usage: py pw_gen.py account=\'name\' len=\'10\' specChar=\'y/n\'')
	sys.exit()
accountStr = sys.argv[1]
lenStr = sys.argv[2]
specCharStr = sys.argv[3]
account = accountStr.partition('account=')[2]
length = int(lenStr.partition('len=')[2])
if(length < 8):
	print('Minimum length must be 8 characters long')
	sys.exit()
specChar = specCharStr.partition('specChar=')[2]

def randomizePW(length, specChar):
	pw = ''
	if(specChar == 'y'):
		for x in range(length):
			num = random.randrange(33, 126)
			if(x == 0):
				if(num != 45 and num != 46):
					pw += chr(num)
				else:
					pw += chr(random.randrange(47, 126))
			else:
				pw += chr(num)
	else:
		for x in range(length):
			cat = int(random.randrange(0, 3))
			if(cat == 0):
				pw += chr(random.randrange(48, 57))
			if(cat == 1):
				pw += chr(random.randrange(65, 90))
			if(cat == 2):
				pw += chr(random.randrange(97, 122))
	return pw

pwFile = open('passwords.txt','a')
pwFile.write('Account: %s  pw: %s\n' % (account, randomizePW(length, specChar)))
pwFile.close()

