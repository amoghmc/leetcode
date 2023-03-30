#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
	Input: nums = [100,4,200,1,3,2]
	Output: 4
	Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
	Therefore its length is 4.

Example 2:
	Input: nums = [0,3,7,2,5,8,4,6,0,1]
	Output: 9

Constraints:
	0 <= nums.length <= 105
	-109 <= nums[i] <= 109

https://leetcode.com/problems/longest-consecutive-sequence/
"""
import unittest


class Solution:
	def longestConsecutive(self, nums):
		# if empty return 0
		if not nums:
			return 0

		nums.sort()

		longest_streak = 1
		current_streak = 1

		for i in range(1, len(nums)):
			if nums[i] != nums[i - 1]:
				if nums[i] == nums[i - 1] + 1:
					current_streak += 1
				else:
					current_streak = 1

				longest_streak = max(longest_streak, current_streak)

		return longest_streak


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.longestConsecutive]
		for my_function in my_functions:
			self.assertEqual(my_function([100, 4, 200, 1, 3, 2]), 4)
			self.assertEqual(my_function([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)


if __name__ == '__main__':
	unittest.main()
