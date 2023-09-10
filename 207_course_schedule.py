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


class Solution(object):
	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""

		# hashmap of all prerequisites for a course
		pre_req_dict = {i: [] for i in range(numCourses)}
		for course, pre_req in prerequisites:
			pre_req_dict[course].append(pre_req)

		visited = set()

		def dfs(course):
			# cycle detected
			if course in visited:
				return False
			# no prerequisites required
			if len(pre_req_dict[course]) == 0:
				return True

			visited.add(course)

			for pre_req in pre_req_dict[course]:
				if not dfs(pre_req):
					return False

			visited.remove(course)
			pre_req_dict[course].clear()
			return True

		for course in range(numCourses):
			if not dfs(course):
				return False

		return True


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.canFinish]
		for my_function in my_functions:
			self.assertEqual(my_function(2, [[1, 0]]), True)
			self.assertEqual(my_function(2, [[1, 0], [0, 1]]), False)


if __name__ == '__main__':
	unittest.main()
