#!/home/linuxbrew/.linuxbrew/bin/python3
"""
You are given an integer array nums.
You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
	Input: nums = [2,3,1,1,4]
	Output: true
	Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
	Input: nums = [3,2,1,0,4]
	Output: false
	Explanation: You will always arrive at index 3 no matter what.
	Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
	1 <= nums.length <= 104
	0 <= nums[i] <= 105

https://leetcode.com/problems/jump-game/
"""
import unittest
from enum import Enum
from typing import List


class Index(Enum):
	GOOD = 0
	BAD = 1
	UNKNOWN = 2


class Solution:
	def canJump(self, nums: List[int]) -> bool:
		goal = len(nums) - 1
		# keep decreasing the goal post
		for i in range(goal - 1, -1, -1):
			# if ith_index + jump_value >= goal_post
			if (i + nums[i]) >= goal:
				goal = i
		return goal == 0

	def canJump_dp(self, nums: List[int]) -> bool:
		last_pos = len(nums) - 1
		cache = {last_pos: True}

		def dfs(pos: int) -> bool:
			nonlocal nums, cache
			if pos in cache:
				return cache[pos]

			max_jump_index = min(last_pos, pos + nums[pos])
			for i in range(pos + 1, max_jump_index + 1):
				if dfs(i):
					cache[i] = True
					return True

			cache[pos] = False
			return False

		return dfs(0)


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.canJump_dp, sol_class.canJump]
		for my_function in my_functions:
			self.assertEqual(my_function([2, 3, 1, 1, 4]), True)
			self.assertEqual(my_function([3, 2, 1, 0, 4]), False)


if __name__ == '__main__':
	unittest.main()
