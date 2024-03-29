#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given the root of a binary tree,
return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).


Example 1:
	Input: root = [3,9,20,null,null,15,7]
	Output: [[3],[9,20],[15,7]]

Example 2:
	Input: root = [1]
	Output: [[1]]

Example 3:
	Input: root = []
	Output: []

Constraints:
	The number of nodes in the tree is in the range [0, 2000].
	-1000 <= Node.val <= 1000

https://leetcode.com/problems/binary-tree-level-order-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		levels = []
		# base case of empty tree
		if not root:
			return levels

		def helper(node, level):
			nonlocal levels
			# if new level then create empty list
			if len(levels) == level:
				levels.append([])

			# append the current node value
			levels[level].append(node.val)

			# process child nodes for the next level
			if node.left:
				helper(node.left, level + 1)
			if node.right:
				helper(node.right, level + 1)

		helper(root, 0)
		return levels
