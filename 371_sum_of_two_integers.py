#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given two integers a and b,
return the sum of the two integers
without using the operators + and -.


Example 1:
	Input: a = 1, b = 2
	Output: 3

Example 2:
	Input: a = 2, b = 3
	Output: 5


Constraints:
-1000 <= a, b <= 1000

https://leetcode.com/problems/sum-of-two-integers/
"""
import unittest


class Solution:
	def getSum(self, a: int, b: int) -> int:
		# 32-bit number containing all 1s
		mask = 0xffffffff

		# while there is no carry
		while b != 0:
			# get the carry after (AND with left shift)
			carry = ((a & b) << 1) & mask
			# sum without carry using XOR
			a = (a ^ b) & mask
			b = carry

		# if a > (31-bit number containing all 1s)
		# as this is the largest positive 32-bit no
		if a > (mask >> 1):
			# take NOT after flipping rightmost 32-bits
			return ~ (a ^ mask)
		else:
			return a


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.getSum]
		for my_function in my_functions:
			self.assertEqual(my_function(3, 9), 12)
			self.assertEqual(my_function(-3, 9), 6)
			self.assertEqual(my_function(-3, -3), -6)
			self.assertEqual(my_function(5, -9), -4)
			self.assertEqual(my_function(-9, 9), 0)


if __name__ == '__main__':
	unittest.main()
