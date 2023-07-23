#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an m x n integer matrix matrix, if an element is 0,
 set its entire row and column to 0's.

You must do it in place.

Example 1:
	Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
	Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
	Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
	Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:
	m == matrix.length
	n == matrix[0].length
	1 <= m, n <= 200
	-231 <= matrix[i][j] <= 231 - 1

https://leetcode.com/problems/set-matrix-zeroes/
"""
from typing import List


class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		rows = len(matrix)
		clms = len(matrix[0])
		zero_rows = set()
		zero_clms = set()

		# add all rows and columns with 0s
		for i in range(rows):
			for j in range(clms):
				if matrix[i][j] == 0:
					zero_rows.add(i)
					zero_clms.add(j)

		# set columns 0
		for j in range(clms):
			if j in zero_clms:
				for i in range(rows):
					matrix[i][j] = 0

		# set rows 0
		for i in range(rows):
			if i in zero_rows:
				for j in range(clms):
					matrix[i][j] = 0

		return
