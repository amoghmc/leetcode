#!/home/linuxbrew/.linuxbrew/bin/python3
"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
	Input: nums = [1,2,3,1]
	Output: 4
	Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
	Total amount you can rob = 1 + 3 = 4.

Example 2:
	Input: nums = [2,7,9,3,1]
	Output: 12
	Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
	Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
	1 <= nums.length <= 100
	0 <= nums[i] <= 400

https://leetcode.com/problems/house-robber/
"""
import unittest
from typing import List


class Solution:
	# similar to max-weight independent set
	def rob(self, nums: List[int]) -> int:
		a, b = 0, 0

		for i in nums:
			a, b = b, max(a + i, b)

		return b

	def rob_list(self, nums: List[int]) -> int:
		dp = [0, nums[0]]

		for i in range(1, len(nums)):
			dp.append(max(dp[i], dp[i - 1] + nums[i]))

		return dp[len(nums)]


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.rob, sol_class.rob_list]
		for my_function in my_functions:
			self.assertEqual(my_function([4]), 4)
			self.assertEqual(my_function([1, 2, 3, 1]), 4)
			self.assertEqual(my_function([2, 7, 9, 3, 1]), 12)


if __name__ == '__main__':
	unittest.main()
