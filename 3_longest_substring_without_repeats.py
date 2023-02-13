#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given a string s, find the length of the longest substring
without repeating characters.

Example 1:
	Input: s = "abcabcbb"
	Output: 3
	Explanation: The answer is "abc", with the length of 3.

Example 2:
	Input: s = "bbbbb"
	Output: 1
	Explanation: The answer is "b", with the length of 1.

Example 3:
	Input: s = "pwwkew"
	Output: 3
	Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
	0 <= s.length <= 5 * 104
	s consists of English letters, digits, symbols and spaces.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
import unittest


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		max_size = i = j = 0
		seen_set = set()

		while i < len(s) and j < len(s):
			if s[j] in seen_set:
				seen_set.remove(s[i])
				i += 1
			else:
				seen_set.add(s[j])
				j += 1
			if len(seen_set) > max_size:
				max_size = len(seen_set)

		return max_size


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.lengthOfLongestSubstring]
		for my_function in my_functions:
			self.assertEqual(my_function("abcabcbb"), 3)
			self.assertEqual(my_function("bbbbb"), 1)
			self.assertEqual(my_function("pwwkew"), 3)


if __name__ == '__main__':
	unittest.main()
