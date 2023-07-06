#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an integer array nums, return the length of the
longest strictly increasing subsequence.


Example 1:
	Input: nums = [10,9,2,5,3,7,101,18]
	Output: 4
	Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
	Input: nums = [0,1,0,3,2,3]
	Output: 4

Example 3:
	Input: nums = [7,7,7,7,7,7,7]
	Output: 1


Constraints:
	1 <= nums.length <= 2500
	-104 <= nums[i] <= 104

https://leetcode.com/problems/longest-increasing-subsequence/
"""
import unittest
from typing import List


class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		lis_for_i = [1 for _ in range(len(nums))]

		for i in range(len(nums) - 1, -1, -1):
			for j in range(i + 1, len(nums)):
				if nums[i] < nums[j]:
					lis_for_i[i] = max(lis_for_i[i], lis_for_i[j] + 1)

		return max(lis_for_i)


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.lengthOfLIS]
		for my_function in my_functions:
			self.assertEqual(my_function([10, 9, 2, 5, 3, 7, 101, 18]), 4)
			self.assertEqual(my_function([0, 1, 0, 3, 2, 3]), 4)
			self.assertEqual(my_function([7, 7, 7, 7, 7, 7, 7]), 1)


if __name__ == '__main__':
	unittest.main()
