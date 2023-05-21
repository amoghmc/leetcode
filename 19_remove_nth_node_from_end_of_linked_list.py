#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
	Input: head = [1,2,3,4,5], n = 2
	Output: [1,2,3,5]

Example 2:
	Input: head = [1], n = 1
	Output: []

Example 3:
	Input: head = [1,2], n = 1
	Output: [1]

Constraints:
	The number of nodes in the list is sz.
	1 <= sz <= 30
	0 <= Node.val <= 100
	1 <= n <= sz
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

		# determine node to be deleted
		length_of_ll = 0
		curr = head
		while curr:
			length_of_ll += 1
			curr = curr.next
		target = length_of_ll - n

		# if first node is to be deleted
		if target == 0:
			head = head.next
			return head

		# if middle or last node is to be deleted
		i = 0
		curr = head
		while curr:
			if i == target - 1:
				curr.next = curr.next.next
			curr = curr.next
			i += 1

		return head
