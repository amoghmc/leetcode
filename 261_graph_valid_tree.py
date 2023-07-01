#!/home/linuxbrew/.linuxbrew/bin/python3
"""
You have a graph of n nodes labeled from 0 to n - 1.
You are given an integer n and a list of edges where
edges[i] = [ai, bi] indicates that there is an undirected edge
between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree,
and false otherwise.


Example 1:
	Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
	Output: true

Example 2:
	Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
	Output: false


Constraints:
	1 <= n <= 2000
	0 <= edges.length <= 5000
	edges[i].length == 2
	0 <= ai, bi < n
	ai != bi
	There are no self-loops or repeated edges.

https://leetcode.com/problems/graph-valid-tree/
"""
import unittest
from typing import List


class Solution:
	def validTree(self, n: int, edges: List[List[int]]) -> bool:
		# empty graph or graph with 1 node is a tree
		if not n or n == 1:
			return True

		# graph with 2 nodes should be connected
		if len(edges) < (n - 1):
			return False

		# node dict containing adjacent nodes
		node_dict = {i: [] for i in range(n)}

		for n1, n2 in edges:
			node_dict[n1].append(n2)
			node_dict[n2].append(n1)

		seen = set()

		def dfs(i, prev):
			nonlocal seen

			# check for cycle
			if i in seen:
				return False
			else:
				seen.add(i)

			for j in node_dict[i]:
				if j == prev:
					continue
				if not dfs(j, i):
					return False

			return True

		return dfs(0, -1) and len(seen) == n


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.validTree]
		for my_function in my_functions:
			self.assertEqual(my_function(5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True)
			self.assertEqual(my_function(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False)


if __name__ == '__main__':
	unittest.main()
