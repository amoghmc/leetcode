#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
	Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
	Output: [1,2,3,6,9,8,7,4,5]

Example 2:
	Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
	Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 10
	-100 <= matrix[i][j] <= 100

https://leetcode.com/problems/spiral-matrix/
"""
import unittest
from typing import List


class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		result = []
		rows, columns = len(matrix), len(matrix[0])
		up = left = 0
		right = columns - 1
		down = rows - 1

		while len(result) < rows * columns:
			# Traverse from left to right.
			# [0, 0] to [0, n - 1]
			for col in range(left, right + 1):
				result.append(matrix[up][col])

			# Traverse downwards.
			# [1, n - 1] to [m - 1, n - 1]
			for row in range(up + 1, down + 1):
				result.append(matrix[row][right])

			# Make sure we are now on a different row.
			if up != down:
				# Traverse from right to left.
				# [m - 1, n - 2] to [m - 1, 0]
				for col in range(right - 1, left - 1, -1):
					result.append(matrix[down][col])

			# Make sure we are now on a different column.
			if left != right:
				# Traverse upwards.
				# [m - 2, 0] to [1, 0]
				for row in range(down - 1, up, -1):
					result.append(matrix[row][left])

			# update boundaries
			up += 1
			right -= 1
			down -= 1
			left += 1

		return result


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.spiralOrder]
		for my_function in my_functions:
			self.assertEqual(my_function([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])
			self.assertEqual(my_function([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
			                 [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])


if __name__ == '__main__':
	unittest.main()
