from time import sleep
import random

# alphabet = '0123456789ABCDE'
alphabet = '0123456789'

codes = []
content = []
length_cipher = 3

chars_crypt = []
chars_decrypt = []

def length_array(choice):
	global length_cipher
	if choice == 1:
		print('Enter length of array: ', end = '')
		length = input()

		# noinspection PyBroadException
		try:
			length = int(length)
		except:
			print('Error')
			sleep(5)
	else:
		print('Drag and drop of array: ', end = '')
		my_array = input().strip('\"')
		try:
			with open(my_array, 'r', encoding = 'utf-8') as f:
				content1 = f.read()
			for l in content1:
				content.append(l)
		except FileNotFoundError:
			print('Error')
			sleep(5)
			exit()
		length = len(content)

	for j in range(0, length):
		while True:
			chars = []
			while True:
				char = random.randint(0, len(alphabet) - 1)
				char = alphabet[char]
				chars.append(char)
				if len(chars) == length_cipher:
					break
				else:
					pass
			chars = ''.join(chars)
			if chars not in codes:
				codes.append(chars)
				break
			else:
				continue
		if num == 2:
			chars_crypt.append("'{0}' : '{1}'".format(content[j], chars))
			chars_decrypt.append("'{0}' : '{1}'".format(chars, content[j]))

	if num == 1:
		for code in codes:
			print(code)

	if num == 2:
		print("\nCrypt\n")
		for i in chars_crypt:
			print(i)
		print("\nDecrypt\n")
		for i in chars_decrypt:
			print(i)

	print('\nThank\'s for you)')
	print('Good luck!')
	sleep(30)


# noinspection PyBroadException
def main():
	# noinspection PyGlobalUndefined
	global num
	print('Enter number of choice:\n\t1) For length of array\n\t2) For elements in array\n')
	choice = input()
	try:
		num = int(choice)
	except:
		main()
	length_array(num)

main()
