#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t
(including duplicates) is included in the window.

If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
	Input: s = "ADOBECODEBANC", t = "ABC"
	Output: "BANC"
	Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
	Input: s = "a", t = "a"
	Output: "a"
	Explanation: The entire string s is the minimum window.

Example 3:
	Input: s = "a", t = "aa"
	Output: ""
	Explanation: Both 'a's from t must be included in the window.
	Since the largest window of s only has one 'a', return empty string.

Constraints:
	m == s.length
	n == t.length
	1 <= m, n <= 105
	s and t consist of uppercase and lowercase English letters.

https://leetcode.com/problems/minimum-window-substring/description/
"""
import unittest


class Solution:
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""

		if not t or not s:
			return ""

		# Dictionary which keeps a count of all the unique characters in t.
		dict_t = {}
		for character in t:
			dict_t[character] = dict_t.get(character, 0) + 1

		# Number of unique characters in t, which need to be present in the desired window.
		required = len(dict_t)

		# left and right pointer
		l_ptr, r_ptr = 0, 0

		# formed is used to keep track of how many unique characters in t are
		# present in the current window in its desired frequency.
		# e.g. if t is "AABC" then the window must have two A's, one B and one C.
		# Thus formed would be = 3 when all these conditions are met.
		formed = 0

		# Dictionary which keeps a count of all the unique characters in the current window.
		window_counts = {}

		# ans tuple of the form (window length, left, right)
		ans = [float("inf"), None, None]

		while r_ptr < len(s):

			# Add one character from the right to the window
			character = s[r_ptr]
			window_counts[character] = window_counts.get(character, 0) + 1

			# If the frequency of the current character added
			# equals to the desired count in t then,
			# increment the formed count by 1.
			if character in dict_t and window_counts[character] == dict_t[character]:
				formed += 1

			# Try and contract the window till the point where it ceases to be 'desirable'.
			while l_ptr <= r_ptr and formed == required:

				# Save the smallest window until now.
				size = r_ptr - l_ptr + 1
				if size < ans[0]:
					ans = [size, l_ptr, r_ptr]

				# The character at the position pointed by the
				# `left` pointer is no longer a part of the window.
				character = s[l_ptr]
				window_counts[character] -= 1
				if character in dict_t and window_counts[character] < dict_t[character]:
					formed -= 1

				# Move the left pointer ahead, this would help to look for a new window.
				l_ptr += 1

			# Keep expanding the window once we are done contracting.
			r_ptr += 1

		if ans[0] == float("inf"):
			return ""
		else:
			return s[ans[1]: ans[2] + 1]


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.minWindow]
		for my_function in my_functions:
			self.assertEqual(my_function("ADOBECODEBANC", "ABC"), "BANC")
			self.assertEqual(my_function("a", "a"), "a")
			self.assertEqual(my_function("a", "aa"), "")


if __name__ == '__main__':
	unittest.main()
