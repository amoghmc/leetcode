#!/home/linuxbrew/.linuxbrew/bin/python3
"""
A trie (pronounced as "try") or prefix tree is a tree data structure
 used to efficiently store and retrieve keys in a dataset of strings.
 There are various applications of this data structure, such as
 autocomplete and spellchecker.

Implement the Trie class:

	- Trie() Initializes the trie object.

	- void insert(String word) Inserts the string word into the trie.

	- boolean search(String word) Returns true if the string word
	is in the trie (i.e., was inserted before), and false otherwise.

	- boolean startsWith(String pfx) Returns true if there is a previously
	inserted string word that has the prefix pfx, and false otherwise.


Example 1:

	Input
	["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
	[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

	Output
	[null, null, true, false, true, null, true]

Explanation
	Trie trie = new Trie();
	trie.insert("apple");
	trie.search("apple");   // return True
	trie.search("app");     // return False
	trie.startsWith("app"); // return True
	trie.insert("app");
	trie.search("app");     // return True


Constraints:
	1 <= word.length, prefix.length <= 2000
	word and prefix consist only of lowercase English letters.
	At most 3 * 104 calls in total will be made to insert, search, and startsWith.

https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class Trie:
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.children = {}
		self.is_end = False

	def insert(self, word: str) -> None:
		"""
		Inserts a word into the trie.
		"""
		node = self
		for char in word:
			# if link doesn't exist, create new link with the missing char
			if char not in node.children:
				node.children[char] = Trie()
			# move down the link recursively
			node = node.children[char]
		node.is_end = True

	def search(self, word: str) -> bool:
		"""
		Returns if the word is in the trie.
		"""
		node = self
		for char in word:
			# if link doesn't exist, as word(link) doesn't exist
			if char not in node.children:
				return False
			# move down the link recursively
			node = node.children[char]

		# return True if word is present and not just a prefix
		return node.is_end

	def startsWith(self, word: str) -> bool:
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		"""
		node = self
		for char in word:
			# if link doesn't exist, as word(link) doesn't exist
			if char not in node.children:
				return False
			# move down the link recursively
			node = node.children[char]

		# prefix is present
		return True
