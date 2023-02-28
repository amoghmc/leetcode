#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an array of strings strs, group the anagrams together.
 You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original letters exactly once.


Example 1:
	Input: strs = ["eat","tea","tan","ate","nat","bat"]
	Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
	Input: strs = [""]
	Output: [[""]]

Example 3:
	Input: strs = ["a"]
	Output: [["a"]]

Constraints:

	1 <= strs.length <= 104
	0 <= strs[i].length <= 100
	strs[i] consists of lowercase English letters.

https://leetcode.com/problems/group-anagrams/
"""
import unittest
from typing import List


class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

		result = []
		result_dict = {}
		for string in strs:
			sorted_str = ''.join(sorted(string))
			if sorted_str in result_dict:
				result_dict[sorted_str].append(string)
			else:
				result_dict[sorted_str] = [string]
		return list(result_dict.values())


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.groupAnagrams]
		for my_function in my_functions:
			self.assertEqual(my_function(["eat", "tea", "tan", "ate", "nat", "bat"]),
			                 [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
			self.assertEqual(my_function([""]), [[""]])
			self.assertEqual(my_function(["a"]), [["a"]])


if __name__ == '__main__':
	unittest.main()
