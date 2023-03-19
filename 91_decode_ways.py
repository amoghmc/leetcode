#!/home/linuxbrew/.linuxbrew/bin/python3
"""
A message containing letters from A-Z can be encoded into numbers
 using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then
 mapped back into letters using the reverse of the mapping above
 (there may be multiple ways).

 For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because
"06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
	Input: s = "12"
	Output: 2
	Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
	Input: s = "226"
	Output: 3
	Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
	Input: s = "06"
	Output: 0
	Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:
	1 <= s.length <= 100
	s contains only digits and may contain leading zero(s).

https://leetcode.com/problems/two-sum/
"""
import unittest
from functools import lru_cache


class Solution:

	@lru_cache(maxsize=None)
	def recursiveWithMemo(self, index, s) -> int:
		# If you reach the end of the string
		# Return 1 for success.
		if index == len(s):
			return 1

		# If the string starts with a zero, it can't be decoded
		if s[index] == '0':
			return 0

		# If the last char of string is between 1-9 inclusive
		if index == len(s) - 1:
			return 1

		answer = self.recursiveWithMemo(index + 1, s)
		if int(s[index: index + 2]) <= 26:
			answer += self.recursiveWithMemo(index + 2, s)

		return answer

	def numDecodings(self, s: str) -> int:
		return self.recursiveWithMemo(0, s)


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.numDecodings]
		for my_function in my_functions:
			self.assertEqual(my_function("12"), 2)
			self.assertEqual(my_function("226"), 3)
			self.assertEqual(my_function("06"), 0)


if __name__ == '__main__':
	unittest.main()
