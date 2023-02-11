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

"""

import unittest
from typing import List


class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		triplets = []
		seen_list = set()
		x = 0
		while x < len(nums):
			if x not in seen_list:
				target = - nums[x]
				two_sum_result = self.twoSum(nums, target)
				if two_sum_result != -1:
					check = False
					for k in two_sum_result:
						if k == x:
							check = True
					if not check:
						two_sum_result.append(x)
						for i in range(len(two_sum_result)):
							seen_list.add(two_sum_result[i])
							two_sum_result[i] = nums[two_sum_result[i]]
							two_sum_result.sort()
						triplets.append(two_sum_result)
			x += 1
		return triplets

	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		hashmap = {}
		for i in range(len(nums)):
			hashmap[nums[i]] = i

		for i in range(len(nums)):
			complement = target - nums[i]
			if complement in hashmap and hashmap[complement] != i:
				return [i, hashmap[complement]]
		return -1


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.threeSum]
		for my_function in my_functions:
			self.assertEqual(my_function([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])
			self.assertEqual(my_function([-1, 1, 0]), [[-1, 0, 1]])
			self.assertEqual(my_function([0, 1, 1]), [])
			self.assertEqual(my_function([0, 0, 0]), [[0, 0, 0]])

			if __name__ == '__main__':
				unittest.main()
