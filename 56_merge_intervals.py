#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.

Example 1:
	Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
	Output: [[1,6],[8,10],[15,18]]
	Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
	Input: intervals = [[1,4],[4,5]]
	Output: [[1,5]]
	Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
	1 <= intervals.length <= 104
	intervals[i].length == 2
	0 <= start <= end <= 104

https://leetcode.com/problems/merge-intervals/
"""
import unittest
from typing import List


class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		i, j = 0, 1
		size = len(intervals)
		check = True
		intervals.sort()

		# while there is a merge keep checking
		while check:
			check = False
			while j < size:
				# jth interval starts after ith interval ends
				if intervals[i][1] >= intervals[j][0]:
					# merge ith and jth interval as ith interval
					intervals[i] = [min(intervals[i][0], intervals[j][0]), max(intervals[i][1], intervals[j][1])]
					# remove jth interval
					intervals.pop(j)
					size -= 1
					check = True
				else:
					i += 1
					j += 1
			i, j = 0, 1
		return intervals


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.merge]
		for my_function in my_functions:
			self.assertEqual(my_function([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
			self.assertEqual(my_function([[1, 4], [4, 5]]), [[1, 5]])


if __name__ == '__main__':
	unittest.main()
