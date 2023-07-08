#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an integer n, return an array ans of length
n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.


Example 1:
	Input: n = 2
	Output: [0,1,1]
	Explanation:
	0 --> 0
	1 --> 1
	2 --> 10

Example 2:
	Input: n = 5
	Output: [0,1,1,2,1,2]
	Explanation:
	0 --> 0
	1 --> 1
	2 --> 10
	3 --> 11
	4 --> 100
	5 --> 101


Constraints:
	0 <= n <= 105

https://leetcode.com/problems/counting-bits/description/
"""
import unittest
from typing import List


class Solution:
	# O(n)
	def countBitsDP(self, n: int) -> List[int]:
		result = [0 for _ in range(n + 1)]

		for i in range(1, n + 1):
			# i  = (1001011101)
			# i' = (100101110)  (ie i' = i / 2)

			# P(i) = P(i / 2) + (i mod 2)
			# result[i] = result[i // 2] + (i % 2)
			result[i] = result[i >> 1] + (i & 1)

		return result

	# O(nlogn)
	def countBits(self, n: int) -> List[int]:
		result = []

		# O(logn)
		def hammingWeight(n: int) -> int:
			result = 0
			while n:
				result += (n % 2)
				# right shift by 1 bit
				n = n >> 1
			return result

		for i in range(n + 1):
			result.append(hammingWeight(i))

		return result


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.countBits, sol_class.countBitsDP]
		for my_function in my_functions:
			self.assertEqual(my_function(2), [0, 1, 1])
			self.assertEqual(my_function(5), [0, 1, 1, 2, 1, 2])


if __name__ == '__main__':
	unittest.main()
