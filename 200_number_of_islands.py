#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an m x n 2D binary grid grid which represents a map
of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
	Input: grid = [
	  ["1","1","1","1","0"],
	  ["1","1","0","1","0"],
	  ["1","1","0","0","0"],
	  ["0","0","0","0","0"]
	]
	Output: 1

Example 2:
	Input: grid = [
	  ["1","1","0","0","0"],
	  ["1","1","0","0","0"],
	  ["0","0","1","0","0"],
	  ["0","0","0","1","1"]
	]
	Output: 3

Constraints:
	m == grid.length
	n == grid[i].length
	1 <= m, n <= 300
	grid[i][j] is '0' or '1'.

https://leetcode.com/problems/number-of-islands/
"""
import unittest
from typing import List


class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		islands = 0
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if grid[i][j] == "1":
					islands += 1
					self.dfs(grid, i, j)
		return islands

	def dfs(self, grid, i, j):
		# if out of bounds then return
		if i < 0 or j < 0 or i == len(grid) or j == len(grid[i]):
			return

		# if seen or in water then return
		if grid[i][j] == "0":
			return

		# don't forget to set the current square to 0 to not come back to it!
		grid[i][j] = "0"

		for row, col in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
			self.dfs(grid, row, col)


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.numIslands]
		for my_function in my_functions:
			self.assertEqual(my_function([
				["1", "1", "1", "1", "0"],
				["1", "1", "0", "1", "0"],
				["1", "1", "0", "0", "0"],
				["0", "0", "0", "0", "0"]
			]), 1)
			self.assertEqual(my_function([
				["1", "1", "0", "0", "0"],
				["1", "1", "0", "0", "0"],
				["0", "0", "1", "0", "0"],
				["0", "0", "0", "1", "1"]
			]), 3)


if __name__ == '__main__':
	unittest.main()
