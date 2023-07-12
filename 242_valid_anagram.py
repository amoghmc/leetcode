#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given two strings s and t, return true
if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging
the letters of a different word or phrase,
typically using all the original letters exactly once.


Example 1:
	Input: s = "anagram", t = "nagaram"
	Output: true

Example 2:
	Input: s = "rat", t = "car"
	Output: false


Constraints:
	1 <= s.length, t.length <= 5 * 104
	s and t consist of lowercase English letters.

https://leetcode.com/problems/valid-anagram/
"""
import unittest


class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		seen = []
		for char in s:
			seen.append(char)

		for char in t:
			if char in seen:
				seen.remove(char)
			else:
				return False

		return len(seen) == 0


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.isAnagram]
		for my_function in my_functions:
			self.assertEqual(my_function("anagram", "nagaram"), True)
			self.assertEqual(my_function("car", "rat"), False)


if __name__ == '__main__':
	unittest.main()
