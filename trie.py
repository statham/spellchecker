class Trie:
	def __init__(self):
		self.word = None
		self.children = {}

	def insert(self, word):
		node = self
		for letter in word:
			if letter.lower() not in node.children:
				node.children[letter.lower()] = Trie()
			node = node.children[letter.lower()]
		node.word = word

	def get(self, word):
		node = self
		for letter in word:
			if letter not in node.children:
				return None
			node = node.children[letter]
		if node.word:
			return node.word
		return None
