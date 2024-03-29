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
		nums_set = set(nums)
		max_len = 0

		for n in nums:
			# check if start of a new sequence
			if n - 1 not in nums_set:
				curr_len = 1

				# find the length of the sequence
				while n + curr_len in nums_set:
					curr_len += 1

				max_len = max(curr_len, max_len)

		return max_len


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.longestConsecutive]
		for my_function in my_functions:
			self.assertEqual(my_function([100, 4, 200, 1, 3, 2]), 4)
			self.assertEqual(my_function([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)


if __name__ == '__main__':
	unittest.main()
