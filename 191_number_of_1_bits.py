#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Write a function that takes the binary representation of an unsigned integer
 and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:
	Input: n = 00000000000000000000000000001011
	Output: 3
	Explanation: The input binary string 00000000000000000000000000001011
	has a total of three '1' bits.

Example 2:
	Input: n = 00000000000000000000000010000000
	Output: 1
	Explanation: The input binary string 00000000000000000000000010000000
	has a total of one '1' bit.

Example 3:
	Input: n = 11111111111111111111111111111101
	Output: 31
	Explanation: The input binary string 11111111111111111111111111111101
	has a total of thirty one '1' bits.

Constraints:
	The input must be a binary string of length 32.

https://leetcode.com/problems/number-of-1-bits/
"""
import unittest


class Solution:
	def hammingWeight(self, n: int) -> int:
		result = 0
		while n:
			# since remainder of odd no is 1
			result += n % 2
			# right shift by 1 bit
			n = n >> 1
		return result


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.hammingWeight]
		for my_function in my_functions:
			self.assertEqual(my_function(0b00000000000000000000000000001011), 3)
			self.assertEqual(my_function(0b00000000000000000000000010000000), 1)
			self.assertEqual(my_function(0b11111111111111111111111111111101), 31)


if __name__ == '__main__':
	unittest.main()
