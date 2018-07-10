import json
from difflib import get_close_matches

data = json.load(open('data.json'))

messages = {
	'type_messages': 'Type word that you want find in dictionary: ',
	'word_not_exist': "Word doesn't exists. Please check it double",
	'suggest_message': 'Do you mean %s instead? (Y - Yes, N - No): ',
	'wrong_entry': 'Wrong entry value'
}

def find_word(word):
	word = word.lower()	

	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]		
	else:
		suggest_words = get_close_matches(word, data.keys())

		if len(suggest_words) >= 1:
			answer = input(messages['suggest_message'] % suggest_words[0])			

			if answer == 'Y':
				return data[suggest_words[0]]
			elif answer == 'N':
				return messages['word_not_exist']
			else:
				return messages['wrong_entry']	
		else:
			return messages['word_not_exist']

word = input(messages['type_messages'])

result = find_word(word)

print('')

if type(result) == list:
	for item in result:
		print(item, '\n')
else:
	print(result, '\n')