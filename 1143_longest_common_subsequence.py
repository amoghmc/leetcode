#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given two strings text1 and text2,
return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated
from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence
that is common to both strings.


Example 1:
	Input: text1 = "abcde", text2 = "ace"
	Output: 3
	Explanation: The longest common subsequence is "ace"
	and its length is 3.

Example 2:
	Input: text1 = "abc", text2 = "abc"
	Output: 3
	Explanation: The longest common subsequence is "abc"
	and its length is 3.

Example 3:
	Input: text1 = "abc", text2 = "def"
	Output: 0
	Explanation: There is no such common subsequence,
	so the result is 0.


Constraints:
	1 <= text1.length, text2.length <= 1000
	text1 and text2 consist of only lowercase English characters.

https://leetcode.com/problems/longest-common-subsequence/
"""
import unittest


class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:

		# Make a grid of 0's with len(text2) + 1 columns
		# and len(text1) + 1 rows.
		dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

		# Iterate up each column, starting from the last one.
		for col in reversed(range(len(text2))):
			for row in reversed(range(len(text1))):
				# If the corresponding characters for this cell are the same...
				if text2[col] == text1[row]:
					dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
				# Otherwise they must be different...
				else:
					dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])

		# The original problem's answer is in dp_grid[0][0]. Return it.
		return dp_grid[0][0]


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.longestCommonSubsequence]
		for my_function in my_functions:
			self.assertEqual(my_function("abcde", "ace"), 3)
			self.assertEqual(my_function("abc", "abc"), 3)
			self.assertEqual(my_function("abc", "def"), 0)


if __name__ == '__main__':
	unittest.main()
