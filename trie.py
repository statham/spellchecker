Class Trie:
	def __init__(self):
		self.word = None
		self.children = {}

	def insert(self, word):
		node = self
		for letter in word:
			if letter not in node.children:
				node.childrend[letter] = Trie()
			node = node.children[letter]
		node.word = word

