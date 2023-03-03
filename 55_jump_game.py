#!/home/linuxbrew/.linuxbrew/bin/python3
"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

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
		last_pos = len(nums) - 1
		for i in range(last_pos - 1, -1, -1):
			if (nums[i] + i) >= last_pos:
				last_pos = i
		return last_pos == 0

	def canJump_dp_top_down(self, nums: List[int]) -> bool:
		memo = [Index.UNKNOWN for _ in range(len(nums))]
		memo[len(nums) - 1] = Index.GOOD
		return self.canJumpFromPositionDpTopDown(0, nums, memo)

	def canJumpFromPositionDpTopDown(self, pos: int, nums: List[int], memo: List[int]) -> bool:
		if memo[pos] != Index.UNKNOWN:
			return memo[pos] == Index.GOOD

		max_jump = min(len(nums) - 1, pos + nums[pos])
		for i in range(pos + 1, max_jump + 1):
			if self.canJumpFromPositionDpTopDown(i, nums, memo):
				memo[i] = Index.GOOD
				return True

		memo[pos] = Index.BAD
		return False


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.canJump_dp_top_down, sol_class.canJump]
		for my_function in my_functions:
			self.assertEqual(my_function([2, 3, 1, 1, 4]), True)
			self.assertEqual(my_function([3, 2, 1, 0, 4]), False)


if __name__ == '__main__':
	unittest.main()
