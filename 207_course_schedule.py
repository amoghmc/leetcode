#!/home/linuxbrew/.linuxbrew/bin/python3
"""
There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0
you have to first take course 1.

Return true if you can finish all courses.
Otherwise, return false.


Example 1:
	Input: numCourses = 2, prerequisites = [[1,0]]
	Output: true
	Explanation: There are a total of 2 courses to take.
	To take course 1 you should have finished course 0.
	So it is possible.

Example 2:
	Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
	Output: false
	Explanation: There are a total of 2 courses to take.
	To take course 1 you should have finished course 0,
	and to take course 0 you should also have finished course 1.
	So it is impossible.

Constraints:
	1 <= numCourses <= 2000
	0 <= prerequisites.length <= 5000
	prerequisites[i].length == 2
	0 <= ai, bi < numCourses
	All the pairs prerequisites[i] are unique.

https://leetcode.com/problems/course-schedule/
"""
import unittest


class Solution:
	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""
		# defaults to [] if key not found
		from collections import defaultdict
		followCourses = defaultdict(list)

		for relation in prerequisites:
			nextCourse, prevCourse = relation[0], relation[1]
			followCourses[prevCourse].append(nextCourse)

		path = [False] * numCourses
		checked = path.copy()

		# check for cycle from each node
		for currCourse in range(numCourses):
			if self.isCyclic(currCourse, followCourses, checked, path):
				return False
		return True

	def isCyclic(self, currCourse, courseDict, checked, path):
		"""   """
		# 1). bottom-cases
		if checked[currCourse]:
			# this node has been checked, no cycle would be formed with this node.
			return False
		if path[currCourse]:
			# came across a marked node in the path, cyclic !
			return True

		# 2). postorder DFS on the children nodes
		# mark the node in the path
		path[currCourse] = True

		ret = False
		# postorder DFS, to visit all its children first.
		for child in courseDict[currCourse]:
			ret = self.isCyclic(child, courseDict, checked, path)
			if ret: break

		# 3). after the visits of children, we come back to process the node itself
		# remove the node from the path
		path[currCourse] = False

		# Now that we've visited the nodes in the downstream,
		#   we complete the check of this node.
		checked[currCourse] = True
		return ret


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.canFinish]
		for my_function in my_functions:
			self.assertEqual(my_function(2, [[1,0]]), True)
			self.assertEqual(my_function(2, [[1,0],[0,1]]), False)


if __name__ == '__main__':
	unittest.main()
