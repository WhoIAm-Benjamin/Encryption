import os
import sys
import pyAesCrypt

direct = []
directory = input('Enter directory for decrypting: ')
password = input('Enter password: ')

def decrypt(file):
    global password
    password = password
    print('-' * 80)
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)
    print("[Decrypt] '" + str(os.path.splitext(file)[0]) + "'")
    os.remove(file)

# noinspection PyShadowingNames
def walk(dir):
	for name in os.listdir(dir):
		path = os.path.join(dir, name)
		if os.path.isfile(path):
			decrypt(path)
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