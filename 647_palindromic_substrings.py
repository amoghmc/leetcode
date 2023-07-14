#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.


Example 1:
	Input: s = "abc"
	Output: 3
	Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
	Input: s = "aaa"
	Output: 6
	Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Constraints:
	1 <= s.length <= 1000
	s consists of lowercase English letters.

https://leetcode.com/problems/palindromic-substrings/
"""
import unittest


class Solution:
	def countSubstrings(self, s: str) -> int:
		result = 0

		def countPalindrome(low, high):
			nonlocal result, s
			while low >= 0 and high < len(s) and s[low] == s[high]:
				low -= 1
				high += 1
				result += 1

		for i in range(len(s)):
			countPalindrome(i, i)
			countPalindrome(i, i + 1)
		return result


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.countSubstrings]
		for my_function in my_functions:
			self.assertEqual(my_function("abc"), 3)
			self.assertEqual(my_function("aaa"), 6)


if __name__ == '__main__':
	unittest.main()
