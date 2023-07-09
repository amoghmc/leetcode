#!/home/linuxbrew/.linuxbrew/bin/python3
"""
You have a graph of n nodes.
You are given an integer n and an array edges where
edges[i] = [ai, bi] indicates that there is an edge
between ai and bi in the graph.

Return the number of connected components in the graph.


Example 1:
	Input: n = 5, edges = [[0,1],[1,2],[3,4]]
	Output: 2

Example 2:
	Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
	Output: 1


Constraints:
	1 <= n <= 2000
	1 <= edges.length <= 5000
	edges[i].length == 2
	0 <= ai <= bi < n
	ai != bi
	There are no repeated edges.

https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
"""
import unittest
from typing import List


class Solution:
	def countComponents(self, n: int, edges: List[List[int]]) -> int:
		adj_dict = {node: set() for edge in edges for node in edge}

		# get a set of neighbors for each node
		for edge in edges:
			node_a, node_b = edge[0], edge[1]
			adj_dict[node_a].add(node_b)
			adj_dict[node_b].add(node_a)

		components = 0
		visited = set()

		def dfs(curr_node):
			nonlocal visited, components, adj_dict

			visited.add(curr_node)

			# node does not have any edges
			if curr_node not in adj_dict:
				return

			for adj_node in adj_dict[curr_node]:
				# ensure path does not form cycle
				if adj_node not in visited:
					dfs(adj_node)
			return

		# check for components from all nodes
		for node in range(n):
			if node not in visited:
				components += 1
				dfs(node)

		return components


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.countComponents]
		for my_function in my_functions:
			self.assertEqual(my_function(5, [[0, 1], [1, 2], [3, 4]]), 2)
			self.assertEqual(my_function(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1)


if __name__ == '__main__':
	unittest.main()
