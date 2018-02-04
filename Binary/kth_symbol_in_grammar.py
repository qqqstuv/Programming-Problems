#https://leetcode.com/contest/weekly-contest-70/problems/k-th-symbol-in-grammar/

import math
class Solution:

	def solve(self, N, K, cur):

		total = math.pow(2,N)
		if N == 0:
			return cur
		half = total // 2
		if K > half:
			return self.solve(N - 1, K - half, 0 if cur == 1 else 1)
		else:
			return self.solve(N - 1, K, cur)

	def kthGrammar(self, N, K):
		"""
		:type N: int
		:type K: int
		:rtype: int
		"""
		return self.solve(N, K, 0)
