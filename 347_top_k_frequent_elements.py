#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an integer array nums and an integer k,
return the k most frequent elements.
You may return the answer in any order.


Example 1:
	Input: nums = [1,1,1,2,2,3], k = 2
	Output: [1,2]

Example 2:
	Input: nums = [1], k = 1
	Output: [1]


Constraints:
	1 <= nums.length <= 105
	-104 <= nums[i] <= 104
	k is in the range [1, the number of unique elements in the array].
	It is guaranteed that the answer is unique.

https://leetcode.com/problems/top-k-frequent-elements/
"""
import unittest
from typing import List


class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		from collections import defaultdict
		freq_dict = defaultdict(int)

		for i in nums:
			freq_dict[i] += 1

		# sort dict by values in decreasing order
		sorted_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))

		result = list(sorted_dict.keys())
		return result[:k]


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.topKFrequent]
		for my_function in my_functions:
			self.assertEqual(my_function([1, 1, 1, 2, 2, 3], 2), [1, 2])
			self.assertEqual(my_function([1], 1), [1])


if __name__ == '__main__':
	unittest.main()
