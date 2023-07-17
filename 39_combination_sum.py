#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target.

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.

Two combinations are unique if the frequency of at least one of the
chosen numbers is different.

The test cases are generated such that the number of unique combinations
that sum up to target is less than 150 combinations for the given input.

Example 1:
	Input: candidates = [2,3,6,7], target = 7
	Output: [[2,2,3],[7]]

Explanation:
	2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
	7 is a candidate, and 7 = 7.
	These are the only two combinations.

Example 2:
	Input: candidates = [2,3,5], target = 8
	Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
	Input: candidates = [2], target = 1
	Output: []

Constraints:
	1 <= candidates.length <= 30
	2 <= candidates[i] <= 40
	All elements of candidates are distinct.
	1 <= target <= 40

https://leetcode.com/problems/combination-sum/
"""
import unittest


class Solution(object):
	def combinationSum(self, candidates, target):
		result = []
		candidates.sort()

		def dfs(curr_target, index, path):
			nonlocal result, candidates
			# if we overshoot, we backtrack
			if curr_target < 0:
				return
			# if we hit the target we add to the result
			if curr_target == 0:
				result.append(path)
				return
			# else we try all possible values from
			# ith candidate to last candidate
			for i in range(index, len(candidates)):
				dfs(curr_target - candidates[i], i, path + [candidates[i]])

		dfs(target, 0, [])
		return result


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.combinationSum]
		for my_function in my_functions:
			self.assertEqual(my_function([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
			self.assertEqual(my_function([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
			self.assertEqual(my_function([2], 1), [])


if __name__ == '__main__':
	unittest.main()
