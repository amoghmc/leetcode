#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Reverse bits of a given 32 bits unsigned integer.

Example 1:
	Input: n = 00000010100101000001111010011100
	Output:    964176192 (00111001011110000010100101000000)
	Explanation: The input binary string 00000010100101000001111010011100 represents the
	unsigned integer 43261596, so return 964176192 which its binary representation is
	00111001011110000010100101000000.

Example 2:
	Input: n = 11111111111111111111111111111101
	Output:   3221225471 (10111111111111111111111111111111)
	Explanation: The input binary string 11111111111111111111111111111101 represents the
	unsigned integer 4294967293, so return 3221225471 which its binary representation is
	10111111111111111111111111111111.


Constraints:
	The input must be a binary string of length 32

https://leetcode.com/problems/reverse-bits/
"""
import unittest


class Solution:
	def reverseBits(self, n):
		result, power = 0, 31
		while n:
			# left shift remainder by power bit
			result += (n % 2) << power
			# right shift by 1 bit
			n = n >> 1
			power -= 1
		return result


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.reverseBits]
		for my_function in my_functions:
			self.assertEqual(my_function(0b00000010100101000001111010011100), 964176192)
			self.assertEqual(my_function(0b11111111111111111111111111111101), 3221225471)


if __name__ == '__main__':
	unittest.main()
