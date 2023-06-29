#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an array of meeting time intervals
where intervals[i] = [starti, endi],
determine if a person could attend all meetings.


Example 1:
	Input: intervals = [[0,30],[5,10],[15,20]]
	Output: false

Example 2:
	Input: intervals = [[7,10],[2,4]]
	Output: true


Constraints:
	0 <= intervals.length <= 104
	intervals[i].length == 2
	0 <= starti < endi <= 106

https://leetcode.com/problems/meeting-rooms/
"""
import unittest
from typing import List


class Solution:
	def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
		intervals.sort()

		for i in range(len(intervals) - 1):
			# ensure current meeting ends before next one starts
			if intervals[i][1] > intervals[i + 1][0]:
				return False

		return True


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.canAttendMeetings]
		for my_function in my_functions:
			self.assertEqual(my_function([[0, 30], [5, 10], [15, 20]]), False)
			self.assertEqual(my_function([[7, 10], [2, 4]]), True)


if __name__ == '__main__':
	unittest.main()
