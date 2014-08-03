import sys

def readDict():
  #get words from /usr/share/dict/words
  f = open('/usr/share/dict/words', 'r')
  words = []
  for word in f.read().split('\n'):
	words.append(word)
  return words

def spellcheck(input, words, wordsHash):
  if input not in wordsHash:

    	#tolowercase
	lowercase = input.lower()
	for word in words:
		if (input == word) or (lowercase == word):
			wordsHash[input] = word
			#stop and return

	#repeated letters
	for letter, g in itertools.groupby(input):
		group = list(g)
		if len(group) > 1:
			rep_input = input.replace("".join(group), letter)
			for word in words:
				if rep_input == word:
					wordsHash[input] = word
					#stop and return

	#incorrect vowels
	vowels = 'aeiou'
	for letter in vowels_input:
		if letter in vowels:
			for vowel in vowels:
				vow_input = input.replace(letter, vowel)
				for word in words:
					if vow_input == word:
						wordsHash[input] = word
						#stop and return
			
  return wordsHash[input]

def run():
  #get dictionary
  words = readDict()
  wordsHash = {}

  #take input and return suggestion until killed
  pass
