#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an m x n grid of characters board and a string word,
 return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example 1:
	Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
	Output: true

Example 2:
	Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
	Output: true

Example 3:
	Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
	Output: false

Constraints:
	m == board.length
	n = board[i].length
	1 <= m, n <= 6
	1 <= word.length <= 15
	board and word consists of only lowercase and uppercase English letters.

https://leetcode.com/problems/two-sum/
"""
import unittest


class Solution(object):
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		rows = len(board)
		clms = len(board[0])

		def dfs(row, col, suffix):
			nonlocal board, rows, clms

			# bottom case: we find match for each letter in the word
			if len(suffix) == 0:
				return True

			# if out of bounds return false
			if row < 0 or row == rows or col < 0 or col == clms:
				return False

			# if mismatch or cycle, return false
			if board[row][col] != suffix[0] or board[row][col] == '#':
				return False

			# mark the choice before exploring further.
			board[row][col] = '#'

			# explore the 4 neighbor directions
			ret = False
			for rowOffset, colOffset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
				if dfs(row + rowOffset, col + colOffset, suffix[1:]):
					ret = True

			# revert the marking
			board[row][col] = suffix[0]

			# Tried all directions, and return result
			return ret

		for row in range(rows):
			for col in range(clms):
				if dfs(row, col, word):
					return True

		# no match found after all exploration
		return False


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.exist]
		for my_function in my_functions:
			self.assertEqual(my_function(
				[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"),
				True)
			self.assertEqual(my_function(
				[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
				True)
			self.assertEqual(my_function(
				[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"),
				False)


if __name__ == '__main__':
	unittest.main()
