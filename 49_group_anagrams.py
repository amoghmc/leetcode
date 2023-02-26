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
https://leetcode.com/problems/two-sum/
"""
import unittest


class Solution:
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		hashmap = {}
		for i in range(len(nums)):
			value = nums[i]
			hashmap[value] = i

		for i in range(len(nums)):
			complement = target - nums[i]
			j = hashmap[complement]
			if complement in hashmap and j != i:
				return [i, j]


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.twoSum]
		for my_function in my_functions:
			self.assertEqual(my_function([2, 7, 11, 15], 9), [0, 1])
			self.assertEqual(my_function([3, 2, 4], 6), [1, 2])
			self.assertEqual(my_function([3, 3], 6), [0, 1])


if __name__ == '__main__':
	unittest.main()
