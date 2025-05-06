def removePunctuation(sentence):
	punct = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{','[', ']', '}', ';', ':', '"', ',', '<', '>', ',', '.', '/', '?', '|', "'"]
	result = ""
	
	for char in sentence:
		if char not in punct:
			result += char
	return result
	
sentence = input()
print(removePunctuation(sentence))