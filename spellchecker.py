import sys
import itertools

def readDict():
  #get words from /usr/share/dict/words
  f = open('/usr/share/dict/words', 'r')
  words = []
  for word in f.read().split('\n'):
	words.append(word)
  return words

def lowercase(input, words, wordsHash):
	for word in words:
		if input.lower() == word:
			wordsHash[input] = word
			#stop and return
			break
	return wordsHash

def repeated_letters(input, words, wordsHash):
	for letter, g in itertools.groupby(input):
		group = list(g)
		while group:
			rep_input = input.replace("".join(group), letter)
			for word in words:
				if rep_input == word:
					wordsHash[input] = word
					#stop and return
					return wordsHash
			group = group[:-1]
	return wordsHash

def vowels(input, words, wordsHash):
	vowels = 'aeiouy'
	for letter in input:
		if letter in vowels:
			for vowel in vowels:
				vow_input = input.replace(letter, vowel)
				for word in words:
					if vow_input == word:
						wordsHash[input] = word
						#stop and return
						return wordsHash
	return wordsHash
			
def spellcheck():
  #get dictionary
  words = readDict()
  wordsHash = {}

  #take input and return suggestion until killed
  input = raw_input('> ')
  while input != 'kill':
	if input not in wordsHash:
		#check if word is correct
		for word in words:
			if input == word:
				wordsHash[input] = word
		if input not in wordsHash:
			#apply spelling corrections
			wordsHash = lowercase(input, words, wordsHash)
			if input not in wordsHash:
				wordsHash = repeated_letters(input, words, wordsHash)
				if input not in wordsHash:
					wordsHash = vowels(input, words, wordsHash)
	if input not in wordsHash:
		wordsHash[input] = 'No suggestions'
	sys.stdout.write(wordsHash[input] + '\n')
	input = raw_input('> ')
