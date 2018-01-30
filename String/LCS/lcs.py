# Longest common subsequences problem

memo = dict()

def LCS(A,B):
	key = str(len(A)) + "-" + str(len(B))
	if key in memo:
		return memo[key]
	else:
		value = ""
		if len(A) == 0 or len(B) == 0:
			return 0
		elif A[-1] == B[-1]: # same last character
			value = LCS(A[:-1],B[:-1]) + A[-1]
		else: # different last character
			dec_A = LCS(A[:-1], B)
			dec_B = LCS(A, B[:-1])
			value = (len(dec_A) > (dec_B)) ? dec_A : dec_B
		memo[key] = value
		return value


string_A = "ABCDCDBACDB"
string_B = "ABCDBACBDCBA"

