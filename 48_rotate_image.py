#!/home/linuxbrew/.linuxbrew/bin/python3
"""
You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify
the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
	Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
	Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
	Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
	Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
	n == matrix.length == matrix[i].length
	1 <= n <= 20
	-1000 <= matrix[i][j] <= 1000

https://leetcode.com/problems/rotate-image/
"""
from typing import List


class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		# reverse
		low = 0
		high = len(matrix) - 1
		while low < high:
			matrix[low], matrix[high] = matrix[high], matrix[low]
			low += 1
			high -= 1

		# transpose
		for i in range(len(matrix)):
			# can also be range(i) i.e. 0 to i - 1
			for j in range(i, len(matrix)):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

		return

	def rotate_loop(self, matrix: List[List[int]]) -> None:
		n = len(matrix[0])
		for i in range(n // 2 + n % 2):
			for j in range(n // 2):
				tmp = matrix[n - 1 - j][i]
				matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
				matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
				matrix[j][n - 1 - i] = matrix[i][j]
				matrix[i][j] = tmp
