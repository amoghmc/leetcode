#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an integer array nums, find the
subarray with the largest sum, and return its sum.

Example 1:
	Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
	Output: 6
	Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
	Input: nums = [1]
	Output: 1
	Explanation: The subarray [1] has the largest sum 1.

Example 3:
	Input: nums = [5,4,-1,7,8]
	Output: 23
	Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:
	1 <= nums.length <= 105
	-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

https://leetcode.com/problems/maximum-subarray/description/
"""
import unittest
from typing import List


class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		max_sum = nums[0]
		curr = 0

		for x in nums:
			# if sum so far is negative,
			# then discard prev subarray
			if curr < 0:
				curr = 0
			curr += x
			max_sum = max(max_sum, curr)

		return max_sum

	def maxSubArray_bf(self, nums: List[int]) -> int:
		max_sum = nums[0]
		size = len(nums)

		for i in range(size):
			curr_sum = 0
			for j in range(i, size):
				curr_sum += nums[j]
				if curr_sum > max_sum:
					max_sum = curr_sum
		return max_sum


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.maxSubArray, sol_class.maxSubArray_bf]
		for my_function in my_functions:
			self.assertEqual(my_function([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
			self.assertEqual(my_function([1]), 1)
			self.assertEqual(my_function([5, 4, -1, 7, 8]), 23)


if __name__ == '__main__':
	unittest.main()
