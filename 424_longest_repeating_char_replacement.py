#!/home/linuxbrew/.linuxbrew/bin/python3
"""
You are given a string s and an integer k.
You can choose any character of the string and
change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the
same letter you can get after performing the above operations.


Example 1:
	Input: s = "ABAB", k = 2
	Output: 4
	Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

	Input: s = "AABABBA", k = 1
	Output: 4
	Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
	The substring "BBBB" has the longest repeating letters, which is 4.
	There may exists other ways to achive this answer too.


Constraints:
	1 <= s.length <= 105
	s consists of only uppercase English letters.
	0 <= k <= s.length

https://leetcode.com/problems/longest-repeating-character-replacement/
"""
import unittest


class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		freq_dict = {}
		result = left_ptr = 0

		for right_ptr in range(len(s)):
			freq_dict[s[right_ptr]] = 1 + freq_dict.get(s[right_ptr], 0)
			window_len = right_ptr - left_ptr + 1

			# We check for validity using the following formula
			# right_ptr - left_ptr + 1 − most_freq_char <= k
			is_valid = (window_len - max(freq_dict.values()) <= k)

			# move the start pointer towards right
			# if the current window is invalid
			if not is_valid:
				freq_dict[s[left_ptr]] -= 1
				left_ptr += 1
				window_len -= 1

			# # the window is valid at this point, store length
			# size of the window never decreases
			result = window_len

		return result


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.characterReplacement]
		for my_function in my_functions:
			self.assertEqual(my_function("ABAB", 2), 4)
			self.assertEqual(my_function("ABABBA", 1), 4)


if __name__ == '__main__':
	unittest.main()
