#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given two integer arrays preorder and inorder where preorder is the
 preorder traversal of a binary tree and inorder is the
 inorder traversal of the same tree, construct and return the binary tree.



Example 1:
	Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
	Output: [3,9,20,null,null,15,7]

Example 2:
	Input: preorder = [-1], inorder = [-1]
	Output: [-1]

Constraints:
	1 <= preorder.length <= 3000
	inorder.length == preorder.length
	-3000 <= preorder[i], inorder[i] <= 3000
	preorder and inorder consist of unique values.
	Each value of inorder also appears in preorder.
	preorder is guaranteed to be the preorder traversal of the tree.
	inorder is guaranteed to be the inorder traversal of the tree.

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
		if not preorder or not inorder:
			return None

		# root is always 1st element of preorder list
		root = preorder[0]

		mid = inorder.index(root)
		# preorder [1, root_index], inorder [0, root - 1]
		left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
		# preorder [root_index + 1, end], inorder [root + 1, end]
		right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

		return TreeNode(root, left, right)
