import json

def find_word(data, word):
	word = word.lower()	
	
	if word in data:
		return data[word]
	else:
		return ["Word doesn't exists. Please check it double"]

data = json.load(open('data.json'))

word = input('Type word that you want find in dictionary: ')

result = find_word(data, word)

print('')

for item in result:
	print(item, '\n')