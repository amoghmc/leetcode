#!/home/linuxbrew/.linuxbrew/bin/python3
"""

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
	Input: height = [1,8,6,2,5,4,8,3,7]
	Output: 49

Explanation: The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section)
the container can contain is 49.

Example 2:
	Input: height = [1,1]
	Output: 1


Constraints:
	n == height.length
	2 <= n <= 105
	0 <= height[i] <= 104

https://leetcode.com/problems/container-with-most-water/
"""
import unittest
from typing import List


class Solution:
	def maxArea(self, height: List[int]) -> int:
		max_area = 0
		i = 0
		j = len(height) - 1

		while i < j:
			area = min(height[i], height[j]) * (j - i)
			max_area = max(max_area, area)
			if height[i] <= height[j]:
				i += 1
			else:
				j -= 1

		return max_area

	def maxArea_bf(self, height: List[int]) -> int:
		max_area = 0
		size = len(height)

		for i in range(size):
			for j in range(i + 1, size):
				area = min(height[i], height[j]) * (j - i)
				max_area = max(max_area, area)

		return max_area


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.maxArea_bf, sol_class.maxArea]
		for my_function in my_functions:
			self.assertEqual(my_function([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
			self.assertEqual(my_function([1, 1]), 1)


if __name__ == '__main__':
	unittest.main()
