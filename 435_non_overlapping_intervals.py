#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an array of intervals called intervals where
intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove
to make the rest of the intervals non-overlapping.


Example 1:
	Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
	Output: 1
	Explanation: [1,3] can be removed and the rest
	of the intervals are non-overlapping.

Example 2:
	Input: intervals = [[1,2],[1,2],[1,2]]
	Output: 2
	Explanation: You need to remove two [1,2] to
	make the rest of the intervals non-overlapping.

Example 3:
	Input: intervals = [[1,2],[2,3]]
	Output: 0
	Explanation: You don't need to remove any of the intervals
	since they're already non-overlapping.


Constraints:
	1 <= intervals.length <= 105
	intervals[i].length == 2
	-5 * 104 <= starti < endi <= 5 * 104

https://leetcode.com/problems/non-overlapping-intervals/
"""
import unittest
from typing import List


class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		intervals.sort()
		prev_end = intervals[0][1]
		result = 0

		for start, end in intervals[1:]:
			# if previous interval starts after new one starts
			# then they are overlapping intervals
			if start < prev_end:
				result += 1
				# getting the min end means we are basically
				# removing the one with larger ending
				prev_end = min(end, prev_end)

			# previous interval has finished before new one
			else:
				# move the previous end to current end
				prev_end = end

		return result


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.eraseOverlapIntervals]
		for my_function in my_functions:
			self.assertEqual(my_function([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)
			self.assertEqual(my_function([[1, 2], [1, 2], [1, 2]]), 2)
			self.assertEqual(my_function([[1, 2], [2, 3]]), 0)


if __name__ == '__main__':
	unittest.main()
