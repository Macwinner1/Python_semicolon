'''def rot13_cipher():
	return "Welcome to Rot13 cipher"
	

def get_rot13_cipher(words):'''


letters = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'], ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
words = "Hello, world!"
words = words.lower()
print(words)
new_list = []
for index, value in enumerate(words):
#if words(value) == letters(index):
	print(index, value)
	new_list.append(value)

print(new_list)

for index, value in enumerate(new_list):
	for item in (letters):
		if value == item:
			print(item) 