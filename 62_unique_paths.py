#!/home/linuxbrew/.linuxbrew/bin/python3
"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner
 (i.e., grid[0][0]). The robot tries to move to the bottom-right corner
 (i.e., grid[m - 1][n - 1]).

 The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.


Example 1:
	Input: m = 3, n = 7
	Output: 28

Example 2:
	Input: m = 3, n = 2
	Output: 3
	Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
	1. Right -> Down -> Down
	2. Down -> Down -> Right
	3. Down -> Right -> Down

Constraints:
	1 <= m, n <= 100

https://leetcode.com/problems/unique-paths/
"""
import unittest


class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		# set all values in grid as 1
		grid = [[1] * n for _ in range(m)]

		for row in range(1, m):
			for col in range(1, n):
				grid[row][col] = grid[row - 1][col] + grid[row][col - 1]

		return grid[m - 1][n - 1]


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.uniquePaths]
		for my_function in my_functions:
			self.assertEqual(my_function(3, 7), 28)
			self.assertEqual(my_function(3, 2), 3)


if __name__ == '__main__':
	unittest.main()
