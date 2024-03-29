#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an integer array nums, return an array answer
such that answer[i] is equal to the product of all
the elements of nums except nums[i].

The product of any prefix or suffix of nums is
guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time
and without using the division operation.


Example 1:
	Input: nums = [1,2,3,4]
	Output: [24,12,8,6]

Example 2:
	Input: nums = [-1,1,0,-3,3]
	Output: [0,0,9,0,0]


Constraints:
	2 <= nums.length <= 105
	-30 <= nums[i] <= 30
	The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

https://leetcode.com/problems/product-of-array-except-self/
"""
import unittest
from typing import List


class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		size = len(nums)
		output = [1 for _ in range(size)]

		tmp = 1

		# pass 1 calculate product of all previous items
		for i in range(size):
			output[i] *= tmp
			tmp *= nums[i]

		tmp = 1

		# pass 2 calculate product of all next items
		for i in range(size - 1, -1, -1):
			output[i] *= tmp
			tmp *= nums[i]

		return output


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.productExceptSelf]
		for my_function in my_functions:
			self.assertEqual(my_function([1, 2, 3, 4]), [24, 12, 8, 6])
			self.assertEqual(my_function([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])


if __name__ == '__main__':
	unittest.main()
