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
import string
import unittest


class Solution:
	def isPalindrome(self, s: str) -> bool:
		# ascii_lowercase = abc...xyz
		# digits = 0..9
		abc = string.ascii_lowercase + string.digits

		reduced_s = ""

		# remove non-alphanumeric chars
		for char in s:
			if char.lower() in abc:
				reduced_s += char.lower()

		low, high = 0, len(reduced_s) - 1

		# check palindrome
		while low < high:
			if reduced_s[low].lower == reduced_s[high].lower:
				low += 1
				high -= 1
			else:
				return False

		return True


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
