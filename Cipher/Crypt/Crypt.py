import os
import sys
import pyAesCrypt

direct = []
directory = input('Enter directory for encrypting: ')
password = input('Enter password: ')

def crypt(file):
	global password
	print('-' * 80)
	# enter password and buffer size
	password = str(password)
	buffer_size = 512*1024
	# call def crypt
	pyAesCrypt.encryptFile(str(file), str(file) + '.crp', password, buffer_size)
	print("[Encrypt] '"+str(file)+".crp'")
	# delete of original file
	os.remove(file)

def walk(dir):
	for name in os.listdir(dir):
		path = os.path.join(dir, name)
		if os.path.isfile(path):
			crypt(path)
		else:
			walk(path)

for i in directory:
    direct.append(i)
if direct[0] == '"':
    del direct[0]
if direct[-1] == '"':
    del direct[-1]
direct = ''.join(direct)
walk(direct)
print('-' * 80)
input()
# os.remove(str(sys.argv[0]))