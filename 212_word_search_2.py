#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an m x n board of characters and a list of strings words,
return all words on the board.

Each word must be constructed from letters of sequentially
adjacent cells, where adjacent cells are horizontally or
vertically neighboring.

The same letter cell may not be used more than once in a word.


Example 1:
	Input:  board = [["o","a","a","n"],
					["e","t","a","e"],
					["i","h","k","r"],
					["i","f","l","v"]],
			words = ["oath","pea","eat","rain"]
	Output: ["eat","oath"]

Example 2:
	Input:  board = [["a","b"],["c","d"]],
			words = ["abcb"]
	Output: []


Constraints:
	m == board.length
	n == board[i].length
	1 <= m, n <= 12
	board[i][j] is a lowercase English letter.
	1 <= words.length <= 3 * 104
	1 <= words[i].length <= 10
	words[i] consists of lowercase English letters.
	All the strings of words are unique.

https://leetcode.com/problems/two-sum/
"""
import unittest
from typing import List


class Trie:
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.children = {}
		self.is_end = False
		self.parent = -1
		self.val = ''

	def insert(self, word: str) -> None:
		"""
		Inserts a word into the trie.
		"""
		curr = self
		for char in word:
			# if link doesn't exist, create new link with the missing char
			if char not in curr.children:
				curr.children[char] = Trie()

				# add parent and value
				curr.children[char].parent = curr
				curr.children[char].val = char

			# move down the link recursively
			curr = curr.children[char]
		curr.is_end = True

	def prune_word(self) -> None:
		curr = self
		while len(curr.children) == 0 and curr.parent != -1:
			parent = curr.parent
			del parent.children[curr.val]
			curr = parent


class Solution:

	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		"""
		:type board: List[List[str]]
		:type word: List[str]
		:rtype: bool
		"""
		self.ROWS = len(board)
		self.COLS = len(board[0])
		self.board = board
		self.found = []

		root = Trie()
		for word in words:
			root.insert(word)

		for row in range(self.ROWS):
			for col in range(self.COLS):
				self.dfs(row, col, "", root)

		return self.found

	def dfs(self, row, col, word, node):
		"""
			backtracking with side-effect,
			the matched letter in the board would be marked with "#".
		"""

		# if out of bounds return false
		if row < 0 or row == self.ROWS or col < 0 or col == self.COLS:
			return

		# if word doesn't exist in trie
		if self.board[row][col] not in node.children or self.board[row][col] == '#':
			return

		node = node.children[self.board[row][col]]
		word += self.board[row][col]
		if node.is_end:
			self.found.append(word)
			node.is_end = False
			node.prune_word()

		# mark the choice before exploring further.
		self.board[row][col] = '#'

		# explore the 4 neighbor directions
		for rowOffset, colOffset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
			self.dfs(row + rowOffset, col + colOffset, word, node)

		# revert the marking
		self.board[row][col] = word[-1]

		# Tried all directions, and did not find any match
		return


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.findWords]
		for my_function in my_functions:
			self.assertEqual(my_function([["o", "a", "a", "n"],
			                              ["e", "t", "a", "e"],
			                              ["i", "h", "k", "r"],
			                              ["i", "f", "l", "v"]],
			                             ["oath", "pea", "eat", "rain"]), ["oath", "eat"])
			self.assertEqual(my_function([["a", "b"],
			                              ["c", "d"]],
			                             ["abcb"]), [])


if __name__ == '__main__':
	unittest.main()
