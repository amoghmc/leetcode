#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Design a data structure that supports adding new words
and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.

void addWord(word) Adds word to the data structure,
it can be matched later.

bool search(word) Returns true if there is any string
in the data structure that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.


Example:

	Input
	["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
	[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

	Output
	[null,null,null,null,false,true,true,true]

Explanation
	WordDictionary wordDictionary = new WordDictionary();
	wordDictionary.addWord("bad");
	wordDictionary.addWord("dad");
	wordDictionary.addWord("mad");
	wordDictionary.search("pad"); // return False
	wordDictionary.search("bad"); // return True
	wordDictionary.search(".ad"); // return True
	wordDictionary.search("b.."); // return True


Constraints:
	1 <= word.length <= 25
	word in addWord consists of lowercase English letters.
	word in search consist of '.' or lowercase English letters.
	There will be at most 2 dots in word for search queries.
	At most 104 calls will be made to addWord and search.

https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""


class WordDictionary:
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.children = {}
		self.is_end = False

	def addWord(self, word: str) -> None:
		"""
		Inserts a word into the trie.
		"""
		node = self
		for char in word:
			# if link doesn't exist, create new link with the missing char
			if char not in node.children:
				node.children[char] = WordDictionary()
			# move down the link recursively
			node = node.children[char]
		node.is_end = True

	def search(self, word: str) -> bool:

		def dfs(j, root):
			curr = root
			for i in range(j, len(word)):
				char = word[i]
				if char == ".":
					for child in curr.children.values():
						if dfs(i + 1, child):
							return True
					return False
				elif char not in curr.children:
					return False
				else:
					curr = curr.children[char]
			return curr.is_end

		return dfs(0, self)
