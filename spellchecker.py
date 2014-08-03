import sys
import itertools
from trie import Trie

def readDict():
  #get words from /usr/share/dict/words
  f = open('/usr/share/dict/words', 'r')
  words = Trie()
  for word in f.read().split('\n'):
	words.insert(word)
  return words

def get_possible_words(word):
  #get possible words for duplicate letters
  prev = None
  states = []
  for letter in word:
	new_states = []
	if letter != prev:
		#no duplicate
		if not states:
			states.append(letter)
		else:
			for i in range(0, len(states)):
				states[i] += letter
	else:
		#duplicate, add new states
		for state in states:
			new_states.append(state+letter)
	states += new_states
	prev = letter
  return states
	
def spellcheck():
  #get dictionary
  words = readDict()

  #take input and return suggestion until killed
  input = raw_input('> ').lower()
  while input != 'kill':
  	valid_words = []
	states = get_possible_words(input)
	for state in states:
		if words.contains(state):
			valid_words.append(state)
	if not valid_words:
		output = 'NO SUGGESTION'
	else:
		output = valid_words[0]
	sys.stdout.write(output+'\n')
	input = raw_input('> ').lower()
