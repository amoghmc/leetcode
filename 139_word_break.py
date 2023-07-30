#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note that the same word in the dictionary
may be reused multiple times in the segmentation.

Example 1:
	Input: s = "leetcode", wordDict = ["leet","code"]
	Output: true
	Explanation: Return true because "leetcode"
	can be segmented as "leet code".

Example 2:
	Input: s = "applepenapple", wordDict = ["apple","pen"]
	Output: true
	Explanation: Return true because "applepenapple"
	can be segmented as "apple pen apple".
	Note that you are allowed to reuse a dictionary word.

Example 3:
	Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
	Output: false

Constraints:
	1 <= s.length <= 300
	1 <= wordDict.length <= 1000
	1 <= wordDict[i].length <= 20
	s and wordDict[i] consist of only lowercase English letters.
	All the strings of wordDict are unique.

https://leetcode.com/problems/word-break/
"""
import unittest
from typing import List


class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		pos_cache = {len(s): True}

		def dfs(pos: int) -> int:
			nonlocal pos_cache, wordDict, s
			# valid base case
			if pos in pos_cache:
				return pos_cache[pos]

			result = False
			for word in wordDict:
				# if a word exists at pos
				if (pos + len(word)) <= len(s) and s[pos: pos + len(word)] == word:
					result = dfs(pos + len(word))
				if result:
					break

			# store result in cache
			pos_cache[pos] = result
			return result

		return dfs(0)


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.wordBreak]
		for my_function in my_functions:
			self.assertEqual(my_function("leetcode", ["leet", "code"]), True)
			self.assertEqual(my_function("applepenapple", ["apple", "pen"]), True)
			self.assertEqual(my_function("catsandog",
			                             ["cats", "dog", "sand", "and", "cat"]), False)


if __name__ == '__main__':
	unittest.main()
