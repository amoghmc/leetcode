#!/home/linuxbrew/.linuxbrew/bin/python3
"""
You are given an array of non-overlapping intervals intervals where
intervals[i] = [starti, endi] represent the start and the end of
the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end]
 that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted
in ascending order by starti and intervals still does not have any
overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
	Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
	Output: [[1,5],[6,9]]

Example 2:
	Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
	Output: [[1,2],[3,10],[12,16]]
	Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
	0 <= intervals.length <= 104
	intervals[i].length == 2
	0 <= starti <= endi <= 105
	intervals is sorted by starti in ascending order.
	newInterval.length == 2
	0 <= start <= end <= 105

https://leetcode.com/problems/insert-interval/
"""
import unittest
from typing import List


class Solution:
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		i = 0
		j = 1
		check = True
		intervals.append(newInterval)
		size = len(intervals)
		intervals.sort()
		# while there is a merge keep checking
		while check:
			check = False
			while j < size:
				len_i = len(intervals[i])
				len_j = len(intervals[j])
				if intervals[i][len_i - 1] >= intervals[j][0] and intervals[i][0] <= intervals[j][len_j - 1]:
					intervals[i] = [min(intervals[i][0], intervals[j][0]),
					                max(intervals[i][len_i - 1], intervals[j][len_j - 1])]
					intervals.pop(j)
					size -= 1
					check = True
				else:
					i += 1
					j += 1
			i = 0
			j = 1
		return intervals


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.insert]
		for my_function in my_functions:
			self.assertEqual(my_function([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
			self.assertEqual(my_function([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
			                 [[1, 2], [3, 10], [12, 16]])


if __name__ == '__main__':
	unittest.main()
