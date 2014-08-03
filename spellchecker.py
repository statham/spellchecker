import sys
from trie import Trie

def readDict():
  #get words from /usr/share/dict/words
  f = open('/usr/share/dict/words', 'r')
  words = Trie()
  #load words into trie
  for word in f.read().split('\n'):
	words.insert(word)
  return words

def get_possible_words(word):
  #get all possible words for duplicate letters and incorrect vowels
  prev = None
  states = []
  vowels = 'aeiouy'
  for letter in word:
	new_states = []
	if (letter != prev) and (letter not in vowels):
		#letter is not a duplicate or vowel
		if not states:
			states.append(letter)
		else:
			#add letter onto each possible word
			for i in range(0, len(states)):
				states[i] += letter
	elif letter == prev:
		#duplicate, add new states
		for state in states:
			new_states.append(state+letter)
		states+=new_states
	else:
		#vowel, add new states for each vowel
		if not states:
			states.append(letter)
			for vowel in vowels:
				if letter != vowel:
					states.append(vowel)
		else:
			for state in states:
				for vowel in vowels:
					new_states.append(state+vowel)
			states = new_states
	prev = letter
  return states
	
def spellcheck():
  #get dictionary
  words = readDict()

  #take input and return suggestion until killed
  input = raw_input('> ').lower()
  while input:
  	valid_words = []
	#check if word correctly spelled
	if words.get(input):
		output = words.get(input)
	#look for all possible mispellings
	else:
		states = get_possible_words(input)
		for state in states:
			if words.get(state):
				valid_words.append(words.get(state))
		if not valid_words:
			output = 'NO SUGGESTION'
		else:
			output = valid_words[0]
	sys.stdout.write(output+'\n')
	input = raw_input('> ').lower()
