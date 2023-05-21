#!/home/linuxbrew/.linuxbrew/bin/python3
"""
You are given an array of k linked-lists lists,
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
	Input: lists = [[1,4,5],[1,3,4],[2,6]]
	Output: [1,1,2,3,4,4,5,6]
	Explanation: The linked-lists are:
	[
        1->4->5,
        1->3->4,
        2->6
	]
	merging them into one sorted list:
	1->1->2->3->4->4->5->6

Example 2:
	Input: lists = []
	Output: []

Example 3:
	Input: lists = [[]]
	Output: []

Constraints:
	k == lists.length
	0 <= k <= 104
	0 <= lists[i].length <= 500
	-104 <= lists[i][j] <= 104
	lists[i] is sorted in ascending order.
	The sum of lists[i].length will not exceed 104.

https://leetcode.com/problems/merge-k-sorted-lists/
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		nodes = []
		head = point = ListNode(0)

		# get values of each list
		for ll in lists:
			while ll:
				nodes.append(ll.val)
				ll = ll.next

		# sort and append them to a new linked list
		for x in sorted(nodes):
			point.next = ListNode(x)
			point = point.next

		return head.next
