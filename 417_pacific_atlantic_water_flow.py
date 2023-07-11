#!/home/linuxbrew/.linuxbrew/bin/python3
"""
There is an m x n rectangular island that borders both
the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches
the island's left and top edges, and the Atlantic Ocean touches
the island's right and bottom edges.

The island is partitioned into a grid of square cells.
You are given an m x n integer matrix heights where heights[r][c]
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow
to neighboring cells directly north, south, east, and west if
the neighboring cell's height <= current cell's height.

Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci]
denotes that rain water can flow from cell (ri, ci)
to both the Pacific and Atlantic oceans.


Example 1:
	Input: heights = [[1,2,2,3,5],
					[3,2,3,4,4],
					[2,4,5,3,1],
					[6,7,1,4,5],
					[5,1,1,2,4]]
	Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
	Explanation: The following cells can flow to the
	Pacific and Atlantic oceans, as shown below:
	[0,4]: [0,4] -> Pacific Ocean
	       [0,4] -> Atlantic Ocean
	[1,3]: [1,3] -> [0,3] -> Pacific Ocean
	       [1,3] -> [1,4] -> Atlantic Ocean
	[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
	       [1,4] -> Atlantic Ocean
	[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
	       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
	[3,0]: [3,0] -> Pacific Ocean
	       [3,0] -> [4,0] -> Atlantic Ocean
	[3,1]: [3,1] -> [3,0] -> Pacific Ocean
	       [3,1] -> [4,1] -> Atlantic Ocean
	[4,0]: [4,0] -> Pacific Ocean
	       [4,0] -> Atlantic Ocean
	Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:
	Input: heights = [[1]]
	Output: [[0,0]]
	Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

Constraints:
	m == heights.length
	n == heights[r].length
	1 <= m, n <= 200
	0 <= heights[r][c] <= 105

https://leetcode.com/problems/pacific-atlantic-water-flow/
"""
import unittest
from typing import List


class Solution:
	def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
		# Check if input is empty
		if not matrix or not matrix[0]:
			return []

		# Initialize variables, including sets used to keep track of visited cells
		num_rows, num_cols = len(matrix), len(matrix[0])
		pacific_reachable = set()
		atlantic_reachable = set()

		def dfs(row, col, reachable, prev_height=-1):
			nonlocal num_cols, num_rows, matrix
			# Check that the new cell hasn't already been visited
			if (row, col) in reachable:
				return

			# if out of bounds return false
			if row < 0 or row == num_rows or col < 0 or col == num_cols:
				return

			# Check that the new cell has a higher or equal height,
			# So that water can flow from the new cell to the old cell
			if matrix[row][col] < prev_height:
				return

			# This cell is reachable, so mark it
			reachable.add((row, col))

			# Check all 4 directions
			for row_offset, col_offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
				dfs(row_offset + row, col_offset + col, reachable, matrix[row][col])

		# Loop through each cell adjacent to the oceans and start a DFS
		for i in range(num_rows):
			# first col
			dfs(i, 0, pacific_reachable)
			# last col
			dfs(i, num_cols - 1, atlantic_reachable)
		for i in range(num_cols):
			# first row
			dfs(0, i, pacific_reachable)
			# last row
			dfs(num_rows - 1, i, atlantic_reachable)

		# Find all cells that can reach both oceans, and convert to list
		return list(pacific_reachable.intersection(atlantic_reachable))


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.pacificAtlantic]
		for my_function in my_functions:
			self.assertEqual(my_function(
				[
					[1, 2, 2, 3, 5],
					[3, 2, 3, 4, 4],
					[2, 4, 5, 3, 1],
					[6, 7, 1, 4, 5],
					[5, 1, 1, 2, 4]
				]), [(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)])
			self.assertEqual(my_function(
				[[1]]), [(0, 0)])


if __name__ == '__main__':
	unittest.main()
