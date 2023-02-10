#!/home/linuxbrew/.linuxbrew/bin/python3
"""

Given a string s, return the longest palindromic substring in s.

Example 1:
	Input: s = "babad"
	Output: "bab"

Explanation: "aba" is also a valid answer.

Example 2:
	Input: s = "cbbd"
	Output: "bb"

Constraints:
	1 <= s.length <= 1000
	s consist of only digits and English letters.

"""
import unittest

class Solution:
	def longestPalindrome_dp(self, s: str) -> str:
		palindrome_matrix = [[False] * len(s) for _ in range(len(s))]

		for i in range(len(s)):
			palindrome_matrix[i][i] = True
		longest_palindrome = s[0]

		# for (i = len(s) - 1) to (i = 0)
		for i in range(len(s) - 1, -1, -1):
			# for (j = i + 1) to (j = len(s) - 1)
			for j in range(i + 1, len(s)):
				if s[i] == s[j]:
					if j - i == 1 or palindrome_matrix[i + 1][j - 1] is True:
						palindrome_matrix[i][j] = True
						if len(longest_palindrome) < len(s[i:j + 1]):
							longest_palindrome = s[i:j + 1]

		return longest_palindrome

	def longestPalindrome_bf(self, s: str) -> str:
		i = 0
		max_size = 0
		max_pal = s[0]

		s_len = len(s)
		while i < s_len:
			j = s_len - 1

			while j > i:
				if s[i] == s[j] and self.checkPalindrome(s, i, j):
					if max_size < j - i + 1:
						max_size = j - i + 1
						max_pal = s[i: j + 1]
					break
				else:
					j -= 1

			i += 1

		return max_pal

	def checkPalindrome(self, s: str, i: int, j: int):
		while i < j:
			if s[i] == s[j]:
				i += 1
				j -= 1
			else:
				break

		if (j == i) or (i - j == 1):
			return True

		return False



class TestSolution(unittest.TestCase):
	def tests(self):
		my_functions = [Solution().longestPalindrome_dp, Solution().longestPalindrome_bf]
		for my_function in my_functions:
			self.assertEqual(my_function("cbbd"), "bb")
			self.assertEqual(my_function("cbabd"), "bab")
			self.assertEqual(my_function("accabbd"), "acca")


if __name__ == '__main__':
	unittest.main()
