#!/home/linuxbrew/.linuxbrew/bin/python3
"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k
(1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1],
nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
	Input: nums = [4,5,6,7,0,1,2], target = 0
	Output: 4

Example 2:
	Input: nums = [4,5,6,7,0,1,2], target = 3
	Output: -1

Example 3:
	Input: nums = [1], target = 0
	Output: -1

Constraints:
	1 <= nums.length <= 5000
	-104 <= nums[i] <= 104
	All values of nums are unique.
	nums is an ascending array that is possibly rotated.
	-104 <= target <= 104

https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""
import unittest
from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		left_ptr, right_ptr = 0, len(nums) - 1

		while left_ptr <= right_ptr:
			mid = (left_ptr + right_ptr) // 2
			if target == nums[mid]:
				return mid
			# if left sorted portion
			if nums[left_ptr] <= nums[mid]:
				if target < nums[left_ptr] or target > nums[mid]:
					left_ptr = mid + 1
				else:
					right_ptr = mid - 1
			# if right sorted portion
			else:
				if target > nums[right_ptr] or target < nums[mid]:
					right_ptr = mid - 1
				else:
					left_ptr = mid + 1
		return -1


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.search]
		for my_function in my_functions:
			self.assertEqual(my_function([4, 5, 6, 7, 0, 1, 2], 0), 4)
			self.assertEqual(my_function([4, 5, 6, 7, 0, 1, 2], 3), -1)
			self.assertEqual(my_function([1], 0), -1)


if __name__ == '__main__':
	unittest.main()
