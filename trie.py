Class Trie:
	def __init__(self):
		self.word = None
		self.children = {}

	def insert(self, word):
		node = self
		for letter in word:
			if letter.lower() not in node.children:
				node.childrend[letter.lower()] = Trie()
			node = node.children[letter.lower()]
		node.word = word

