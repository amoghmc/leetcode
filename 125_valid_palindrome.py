#!/home/linuxbrew/.linuxbrew/bin/python3
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
	Input: s = "A man, a plan, a canal: Panama"
	Output: true
	Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
	Input: s = "race a car"
	Output: false
	Explanation: "raceacar" is not a palindrome.

Example 3:
	Input: s = " "
	Output: true
	Explanation: s is an empty string "" after removing non-alphanumeric characters.
	Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:
	1 <= s.length <= 2 * 105
	s consists only of printable ASCII characters.

https://leetcode.com/problems/valid-palindrome/
"""
import unittest


class Solution:
	def isPalindrome(self, s: str) -> bool:
		alphanumeric_list = []
		abc = "abcdefghijklmnopqrstuvwxyz0123456789"
		for char in s:
			if char.lower() in abc:
				alphanumeric_list.append(char.lower())
		converted_str = "".join(alphanumeric_list)
		return converted_str == converted_str[::-1]


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.isPalindrome]
		for my_function in my_functions:
			self.assertEqual(my_function("A man, a plan, a canal: Panama"), 1)
			self.assertEqual(my_function("race a car"), 0)
			self.assertEqual(my_function(" "), 1)


if __name__ == '__main__':
	unittest.main()
