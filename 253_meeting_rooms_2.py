#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an array of meeting time intervals
where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.


Example 1:
	Input: intervals = [[0,30],[5,10],[15,20]]
	Output: 2

Example 2:
	Input: intervals = [[7,10],[2,4]]
	Output: 1


Constraints:
	1 <= intervals.length <= 104
	0 <= starti < endi <= 106

https://leetcode.com/problems/meeting-rooms-ii/
"""
import unittest
from typing import List


class Solution:
	def minMeetingRooms(self, intervals: List[List[int]]) -> int:
		start_arr = [i[0] for i in intervals]
		end_arr = [i[1] for i in intervals]

		start_arr.sort()
		end_arr.sort()

		start_ptr, end_ptr = 0, 0
		tmp, rooms = 0, 0

		while start_ptr < len(start_arr):
			if start_arr[start_ptr] < end_arr[end_ptr]:
				tmp += 1
				start_ptr += 1
			else:
				tmp -= 1
				end_ptr += 1

			rooms = max(tmp, rooms)

		return rooms


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.minMeetingRooms]
		for my_function in my_functions:
			self.assertEqual(my_function([[0, 30], [5, 10], [15, 20]]), 2)
			self.assertEqual(my_function([[7, 10], [2, 4]]), 1)


if __name__ == '__main__':
	unittest.main()
