#!/home/linuxbrew/.linuxbrew/bin/python3
"""
There is a new alien language that uses the English alphabet.
However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary,
where the strings in words are sorted lexicographicallyby the rules
of this new language.

Return a string of the unique letters in the new alien language
sorted in lexicographically increasing order by the new language's rules.

If there is no solution, return "".
If there are multiple solutions, return any of them.


Example 1:
	Input: words = ["wrt","wrf","er","ett","rftt"]
	Output: "wertf"

Example 2:
	Input: words = ["z","x"]
	Output: "zx"

Example 3:
	Input: words = ["z","x","z"]
	Output: ""
	Explanation: The order is invalid, so return "".


Constraints:
	1 <= words.length <= 100
	1 <= words[i].length <= 100
	words[i] consists of only lowercase English letters.

https://leetcode.com/problems/alien-dictionary/
"""
import unittest
from typing import List


class Solution:
	def alienOrder(self, words: List[str]) -> str:
		# dict containing descendants for all chars
		char_children_dict = {char: set() for word in words for char in word}

		for i in range(len(words) - 1):
			word_1, word_2 = words[i], words[i + 1]
			min_len = min(len(word_1), len(word_2))

			# check for invalid order for patterns like [apes, ape]
			if len(word_1) > len(word_2) and word_1[:min_len] == word_2[:min_len]:
				return ""

			for j in range(min_len):
				# if there is mismatch between chars
				if word_1[j] != word_2[j]:
					# add child char to set of parent char's descendants
					char_children_dict[word_1[j]].add(word_2[j])
					break

		# dict where char = false is visited and
		# char = True is visited and is on curr path
		visited = {}
		result = []

		def dfs(char):
			# cycle detected
			if char in visited:
				return visited[char]

			visited[char] = True

			for child in char_children_dict[char]:
				# cycle detected
				if dfs(child):
					return True

			visited[char] = False
			result.append(char)

		for char in char_children_dict:
			# cycle detected
			if dfs(char):
				return ""

		result.reverse()
		return "".join(result)


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.alienOrder]
		for my_function in my_functions:
			self.assertEqual(my_function(["wrt","wrf","er","ett","rftt"]), "wertf")
			self.assertEqual(my_function(["z","x"]), "zx")
			self.assertEqual(my_function(["z","x","z"]), "")


if __name__ == '__main__':
	unittest.main()
