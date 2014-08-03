import sys

def readDict():
  #get words from /usr/share/dict/words
  f = open('/usr/share/dict/words', 'r')
  words = []
  for word in f.read().split('\n'):
	words.append(word)
  return words

def spellcheck(input, words, wordsHash):
  #if word is correct, just return word

  #if incorrect
    #tolowercase
    #repeated letters
    #incorrect vowels

  pass

def run():
  #get dictionary
  words = readDict()
  wordsHash = {}

  #take input and return suggestion until killed
  pass
