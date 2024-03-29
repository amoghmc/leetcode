#!/home/linuxbrew/.linuxbrew/bin/python3
"""

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
	Input: nums = [2,7,11,15], target = 9
	Output: [0,1]
	Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
	Input: nums = [3,2,4], target = 6
	Output: [1,2]

Example 3:
	Input: nums = [3,3], target = 6
	Output: [0,1]


Constraints:
	2 <= nums.length <= 104
	-109 <= nums[i] <= 109
	-109 <= target <= 109
	Only one valid answer exists.

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
		index_dict = {}

		# dict[value] = index
		for i in range(len(nums)):
			value = nums[i]
			index_dict[value] = i

		for i in range(len(nums)):
			complement_value = target - nums[i]
			# check if it is a repeated value
			# ex: dict[3] = 5, target = 10 and output = [3, 3] which is repeated
			if complement_value in index_dict and index_dict[complement_value] != i:
				return [i, index_dict[complement_value]]


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
