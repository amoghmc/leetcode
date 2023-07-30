#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an integer array nums, find a subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
	Input: nums = [2,3,-2,4]
	Output: 6
	Explanation: [2,3] has the largest product 6.

Example 2:
	Input: nums = [-2,0,-1]
	Output: 0
	Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:
	1 <= nums.length <= 2 * 104
	-10 <= nums[i] <= 10
	The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

https://leetcode.com/problems/maximum-product-subarray/
"""
import unittest
from typing import List


class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		if len(nums) == 0:
			return 0

		max_so_far = min_so_far = result = nums[0]

		for n in nums[1:]:
			temp_max = max(n, max_so_far * n, min_so_far * n)

			min_so_far = min(n, max_so_far * n, min_so_far * n)
			max_so_far = temp_max

			result = max(max_so_far, result)

		return result


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.maxProduct]
		for my_function in my_functions:
			self.assertEqual(my_function([2, 3, -2, 4]), 6)
			self.assertEqual(my_function([-2, 0, -1]), 0)


if __name__ == '__main__':
	unittest.main()
