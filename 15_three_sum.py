#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
	Input: nums = [-1,0,1,2,-1,-4]
	Output: [[-1,-1,2],[-1,0,1]]
	Explanation:
	# the below 2 are duplicate triplets
	nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
	nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.

	nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
	The distinct triplets are [-1,0,1] and [-1,-1,2].
	Notice that the order of the output and the order of the triplets does not matter.

Example 2:
	Input: nums = [0,1,1]
	Output: []
	Explanation: The only possible triplet does not sum up to 0.

Example 3:
	Input: nums = [0,0,0]
	Output: [[0,0,0]]
	Explanation: The only possible triplet sums up to 0.

Constraints:
	3 <= nums.length <= 3000
	-105 <= nums[i] <= 105

https://leetcode.com/problems/3sum/
"""

import unittest
from typing import List


class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		res = []
		nums.sort()
		for i in range(len(nums)):
			if nums[i] > 0:
				break
			# check if not solved previously (nums is sorted)
			# ie check if nums[i] is not repeated for prev i
			if i == 0 or nums[i - 1] != nums[i]:
				self.twoSumII(nums, i, res)
		return res

	def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
		low, high = i + 1, len(nums) - 1
		while low < high:
			total = nums[i] + nums[low] + nums[high]
			if total < 0:
				low += 1
			elif total > 0:
				high -= 1
			else:
				res.append([nums[i], nums[low], nums[high]])
				low += 1
				high -= 1
				# skip over repeated numbers
				while low < high and nums[low] == nums[low - 1]:
					low += 1


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.threeSum]
		for my_function in my_functions:
			self.assertEqual(my_function([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
			self.assertEqual(my_function([-1, 1, 0]), [[-1, 0, 1]])
			self.assertEqual(my_function([0, 1, 1]), [])
			self.assertEqual(my_function([0, 0, 0]), [[0, 0, 0]])
			self.assertEqual(my_function([0, 0, 0, 0]), [[0, 0, 0]])


if __name__ == '__main__':
	unittest.main()
