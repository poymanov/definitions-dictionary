import json

def find_word(data, word):
	if word in data:
		return data[word]
	else:
		return ["Word doesn't exists"]

data = json.load(open('data.json'))

word = input('Type word that you want find in dictionary: ')

result = find_word(data, word)

print('')

for item in result:
	print(item, '\n')