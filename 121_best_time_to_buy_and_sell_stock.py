#!/home/linuxbrew/.linuxbrew/bin/python3
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.


Example 1:
	Input: prices = [7,1,5,3,6,4]
	Output: 5
	Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
	Note that buying on day 2 and selling on day 1 is not allowed because
	 you must buy before you sell.

Example 2:
	Input: prices = [7,6,4,3,1]
	Output: 0
	Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
	1 <= prices.length <= 105
	0 <= prices[i] <= 104

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
import unittest
from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		max_profit = 0
		min_so_far = float('inf')

		for i in range(len(prices)):
			min_so_far = min(min_so_far, prices[i])
			max_profit = max(max_profit, prices[i] - min_so_far)

		return max_profit


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.maxProfit]
		for my_function in my_functions:
			self.assertEqual(my_function([7, 1, 5, 3, 6, 4]), 5)
			self.assertEqual(my_function([7, 6, 4, 3, 1]), 0)


if __name__ == '__main__':
	unittest.main()
