#!/home/linuxbrew/.linuxbrew/bin/python3
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example 1:
	Input: n = 2
	Output: 2
	Explanation: There are two ways to climb to the top.
	1. 1 step + 1 step
	2. 2 steps

Example 2:
	Input: n = 3
	Output: 3
	Explanation: There are three ways to climb to the top.
	1. 1 step + 1 step + 1 step
	2. 1 step + 2 steps
	3. 2 steps + 1 step

Constraints:
	1 <= n <= 45

https://leetcode.com/problems/climbing-stairs/
"""
import unittest


class Solution:
	def climbStairs(self, n: int) -> int:
		if n == 1:
			return 1

		dp = [0 for _ in range(n + 1)]
		# ways to climb 1 step
		dp[0] = 1
		# ways to climb 2 steps
		dp[1] = 2

		# fibonacci series
		for i in range(2, n):
			dp[i] = dp[i - 1] + dp[i - 2]

		# return ways to climb n steps
		return dp[n - 1]


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.climbStairs]
		for my_function in my_functions:
			self.assertEqual(my_function(2), 2)
			self.assertEqual(my_function(3), 3)


if __name__ == '__main__':
	unittest.main()
