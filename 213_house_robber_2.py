#!/home/linuxbrew/.linuxbrew/bin/python3
"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.

Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.


Example 1:
	Input: nums = [2,3,2]
	Output: 3
	Explanation: You cannot rob house 1 (money = 2)
	and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
	Input: nums = [1,2,3,1]
	Output: 4
	Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
	Total amount you can rob = 1 + 3 = 4.

Example 3:
	Input: nums = [1,2,3]
	Output: 3


Constraints:
	1 <= nums.length <= 100
	0 <= nums[i] <= 1000

https://leetcode.com/problems/house-robber-ii/
"""
import unittest
from typing import List


class Solution:
	def rob(self, nums: List[int]) -> int:
		if len(nums) == 1:
			return nums[0]

		def house_robber_1(nums: List[int]) -> int:
			a, b = 0, 0

			for i in nums:
				a, b = b, max(a + i, b)

			return b

		a = nums[1:]
		b = nums[:-1]
		return max(house_robber_1(a), house_robber_1(b))

	def rob_list(self, nums: List[int]) -> int:
		if len(nums) == 1:
			return nums[0]

		def house_robber_1(nums: List[int]) -> int:
			dp = [0 for _ in range(len(nums) + 1)]
			dp[0] = 0
			dp[1] = nums[0]

			for i in range(2, len(nums) + 1):
				dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

			return dp[len(nums)]

		a = nums[1:]
		b = nums[:-1]
		return max(house_robber_1(a), house_robber_1(b))


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.rob, sol_class.rob_list]
		for my_function in my_functions:
			self.assertEqual(my_function([2, 3, 2]), 3)
			self.assertEqual(my_function([1, 2, 3, 1]), 4)
			self.assertEqual(my_function([1, 2, 3]), 3)


if __name__ == '__main__':
	unittest.main()
