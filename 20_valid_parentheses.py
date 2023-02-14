#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
	Input: s = "()"
	Output: true

Example 2:
	Input: s = "()[]{}"
	Output: true

Example 3:
	Input: s = "(]"
	Output: false

Constraints:
	1 <= s.length <= 104
	s consists of parentheses only '()[]{}'.

https://leetcode.com/problems/valid-parentheses/
"""
import unittest


class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		paren_dict = {"]": "[", "}": "{", ")": "("}
		for char in s:
			# if opening parenthesis
			if char in paren_dict.values():
				stack.append(char)
			# if closing parenthesis
			else:
				if stack == [] or paren_dict[char] != stack.pop():
					return False
		return stack == []


class TestSolution(unittest.TestCase):
	def tests(self):
		sol_class = Solution()
		my_functions = [sol_class.isValid]
		for my_function in my_functions:
			self.assertEqual(my_function("()"), True)
			self.assertEqual(my_function("()[]{}"), True)
			self.assertEqual(my_function("(}"), False)


if __name__ == '__main__':
	unittest.main()
