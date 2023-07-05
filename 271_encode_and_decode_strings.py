#!/home/linuxbrew/.linuxbrew/bin/python3
"""
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded
back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}

Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}

So Machine 1 does:
string encoded_string = encode(strs);

and Machine 2 does:
vector<string> strs2 = decode(encoded_string);

strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).


Example 1:

	Input: dummy_input = ["Hello","World"]
	Output: ["Hello","World"]

	Explanation:
	Machine 1:
	Codec encoder = new Codec();
	String msg = encoder.encode(strs);
	Machine 1 ---msg---> Machine 2

	Machine 2:
	Codec decoder = new Codec();
	String[] strs = decoder.decode(msg);

Example 2:
	Input: dummy_input = [""]
	Output: [""]


Constraints:

	1 <= strs.length <= 200
	0 <= strs[i].length <= 200
	strs[i] contains any possible characters out of 256 valid ASCII characters.

https://leetcode.com/problems/encode-and-decode-strings/
"""
from typing import List


class Codec:
	def encode(self, strs: List[str]) -> str:
		"""Encodes a list of strings to a single string
		"""
		result = ""
		for word in strs:
			# add len of word with # as delimiter
			# ex: ["bat", "book"]  -> "3#bat4#book"
			result += str(len(word)) + "#" + word
		return result

	def decode(self, s: str) -> List[str]:
		"""Decodes a single string to a list of strings.
		"""
		res, i = [], 0
		while i < len(s):
			j = i
			# reach till delimiter
			while s[j] != "#":
				j += 1

			# get the encoded length of next word
			length = int(s[i:j])
			# get starting index of next word,
			# skipping the delimiter #
			index_after_delim = j + 1

			res.append(s[index_after_delim: index_after_delim + length])
			i = index_after_delim + length
		return res
