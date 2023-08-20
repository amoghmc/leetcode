#!/home/linuxbrew/.linuxbrew/bin/python3
"""
You are given an integer array coins representing coins
of different denominations and an integer amount
representing a total amount of money.

Return the fewest number of coins that you need
to make up that amount. If that amount of money cannot
be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:
	Input: coins = [1,2,5], amount = 11
	Output: 3
	Explanation: 11 = 5 + 5 + 1

Example 2:
	Input: coins = [2], amount = 3
	Output: -1

Example 3:
	Input: coins = [1], amount = 0
	Output: 0


Constraints:
	1 <= coins.length <= 12
	1 <= coins[i] <= 231 - 1
	0 <= amount <= 104

https://leetcode.com/problems/coin-change/
"""
import unittest
from typing import List


class Solution:
	def coinChange_DFS(self, coins: List[int], amount: int) -> int:
		cache = {0: 0}
		coins.sort()

		def dfs(amount: int) -> int:
			nonlocal coins, cache
			if amount in cache:
				return cache[amount]

			ans = float('inf')
			for i in coins:
				if amount - i < 0:
					break
				ans = min(ans, 1 + dfs(amount - i))

			cache[amount] = ans
			return ans

		ans = dfs(amount)
		if ans == float('inf'):
			return -1
		return ans

	def coinChange(self, coins: List[int], amount: int) -> int:
		coin_change_for_i = [(amount + 1) for _ in range(amount + 1)]
		coin_change_for_i[0] = 0

		for curr_amount in range(1, amount + 1):
			for coin in coins:
				remaining = curr_amount - coin
				if remaining >= 0:
					coin_change_for_i[curr_amount] = min(coin_change_for_i[curr_amount],
					                                     coin_change_for_i[remaining] + 1)

		if coin_change_for_i[amount] == amount + 1:
			return -1
		else:
			return coin_change_for_i[amount]


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.coinChange, sol_class.coinChange_DFS]
		for my_function in my_functions:
			self.assertEqual(my_function([1, 2, 5], 11), 3)
			self.assertEqual(my_function([2], 3), -1)
			self.assertEqual(my_function([1], 0), 0)


if __name__ == '__main__':
	unittest.main()
