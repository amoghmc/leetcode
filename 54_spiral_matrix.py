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
		left, right = 0, len(matrix[0])
		top, bottom = 0, len(matrix)

		while left < right and top < bottom:
			# get every i in top row
			for i in range(left, right):
				result.append(matrix[top][i])
			top += 1

			# get every i in right col
			for i in range(top, bottom):
				result.append(matrix[i][right - 1])
			right -= 1

			if left >= right or top >= bottom:
				break

			# get every i in bottom row
			for i in range(right - 1, left - 1, -1):
				result.append(matrix[bottom - 1][i])
			bottom -= 1

			# get every i in left col
			for i in range(bottom - 1, top - 1, -1):
				result.append(matrix[i][left])
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
