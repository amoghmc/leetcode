#!/home/linuxbrew/.linuxbrew/bin/python3
"""
The median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.
Answers within 10-5 of the actual answer will be accepted.


Example 1:
	Input
	["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
	[[], [1], [2], [], [3], []]

	Output
	[null, null, null, 1.5, null, 2.0]

	Explanation
	MedianFinder medianFinder = new MedianFinder();
	medianFinder.addNum(1);    // arr = [1]
	medianFinder.addNum(2);    // arr = [1, 2]
	medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
	medianFinder.addNum(3);    // arr[1, 2, 3]
	medianFinder.findMedian(); // return 2.0


Constraints:
	-105 <= num <= 105
	There will be at least one element in the data structure before calling findMedian.
	At most 5 * 104 calls will be made to addNum and findMedian.

https://leetcode.com/problems/find-median-from-data-stream/
"""
import heapq


class MedianFinder:

	def __init__(self):
		self.arr = []

	def addNum(self, num: int) -> None:
		self.arr.append(num)

	def findMedian(self) -> float:
		size = len(self.arr)
		self.arr.sort()
		if size % 2 != 0:
			return self.arr[size // 2]
		else:
			total = self.arr[size // 2 - 1] + self.arr[size // 2]
			return total / 2


class MedianFinderTwoHeaps:

	def __init__(self):
		# implemented as MaxHeap
		self.less_than_mid = []

		# implemented as MinHeap
		self.greater_than_mid = []

	def addNum(self, num: int) -> None:
		less_than_mid = self.less_than_mid
		greater_than_mid = self.greater_than_mid

		heapq.heappush(less_than_mid, -1 * num)

		if less_than_mid and greater_than_mid \
			and ((-1 * less_than_mid[0]) > greater_than_mid[0]):
			val = heapq.heappop(less_than_mid) * -1
			heapq.heappush(greater_than_mid, val)

		if len(less_than_mid) > len(greater_than_mid) + 1:
			val = heapq.heappop(less_than_mid) * -1
			heapq.heappush(greater_than_mid, val)

		elif len(less_than_mid) + 1 < len(greater_than_mid):
			val = heapq.heappop(greater_than_mid) * -1
			heapq.heappush(less_than_mid, val)

	def findMedian(self) -> float:
		less_than_mid = self.less_than_mid
		greater_than_mid = self.greater_than_mid

		if len(greater_than_mid) == len(less_than_mid):
			return (greater_than_mid[0] + (-1 * less_than_mid[0])) / 2
		elif len(greater_than_mid) > len(less_than_mid):
			return greater_than_mid[0]
		else:
			return -1 * less_than_mid[0]
