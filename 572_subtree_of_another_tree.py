#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given the roots of two binary trees root and subRoot,
return true if there is a subtree of root with the same structure
and node values of subRoot and false otherwise.

A subtree of a binary tree called tree is a tree that consists of a node
in tree and all of this node's descendants.
The tree called tree could also be considered as a subtree of itself.


Example 1:
	Input: root = [3,4,5,1,2], subRoot = [4,1,2]
	Output: true

Example 2:
	Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
	Output: false


Constraints:
	The number of nodes in the root tree is in the range [1, 2000].
	The number of nodes in the subRoot tree is in the range [1, 1000].
	-104 <= root.val <= 104
	-104 <= subRoot.val <= 104

https://leetcode.com/problems/subtree-of-another-tree/
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

		def dfs(a, b):
			if a is None and b is None:
				return True
			elif a is None or b is None:
				return False
			elif a.val == b.val:
				return dfs(a.left, b.left) and dfs(a.right, b.right)
			else:
				return False

		sub_val = subRoot.val
		sub_trees_set = set()

		def find_potential_trees(curr):
			nonlocal sub_val, sub_trees_set
			if curr is None:
				return
			if curr.val == sub_val:
				sub_trees_set.add(curr)
			find_potential_trees(curr.left)
			find_potential_trees(curr.right)

		find_potential_trees(root)
		while sub_trees_set:
			if dfs(sub_trees_set.pop(), subRoot):
				return True
