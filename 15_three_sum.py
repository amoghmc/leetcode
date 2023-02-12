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


class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums.sort()
		size, result = len(nums), []
		for i in range(size):

			# check if i is solved previously
			if i > 0 and nums[i] == nums[i - 1]:
				continue

			target = - nums[i]
			j, k = i + 1, size - 1
			while j < k:
				two_sum = nums[j] + nums[k]
				if two_sum == target:
					triplet = [nums[i], nums[j], nums[k]]
					triplet.sort()
					result.append(triplet)

					j += 1
					# check if j is solved previously
					while j < k and nums[j] == nums[j - 1]:
						j += 1

				# if sum < target
				elif two_sum < target:
					j += 1
				# if sum > target
				else:
					k -= 1
		return result


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
