#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.


Example 1:
	Input: nums = [1,2,3,1]
	Output: true

Example 2:
	Input: nums = [1,2,3,4]
	Output: false

Example 3:
	Input: nums = [1,1,1,3,3,4,3,2,4,2]
	Output: true


Constraints:
	1 <= nums.length <= 105
	-109 <= nums[i] <= 109

https://leetcode.com/problems/contains-duplicate/
"""
import unittest
from typing import List


class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		seen = set()
		for i in nums:
			if i not in seen:
				seen.add(i)
			else:
				return True
		return False


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.containsDuplicate]
		for my_function in my_functions:
			self.assertEqual(my_function([1, 2, 3, 1]), True)
			self.assertEqual(my_function([1, 2, 3, 4]), False)
			self.assertEqual(my_function([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)


if __name__ == '__main__':
	unittest.main()
