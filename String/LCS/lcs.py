# Longest common subsequences problem

memo = dict()

def LCS(A,B):
	key = str(len(A)) + "-" + str(len(B))
	if key in memo:
		return memo[key]
	else:
		value = ""
		if len(A) == 0 or len(B) == 0:
			return ""
		elif A[-1] == B[-1]: # same last character
			value = LCS(A[:-1],B[:-1]) + A[-1]
		else: # different last character
			dec_A = LCS(A[:-1], B)
			dec_B = LCS(A, B[:-1])
			value = dec_A if (len(dec_A) > len(dec_B))  else dec_B
		memo[key] = value
		return value

def LCS_retrieveAllString(A,B):
	key = str(len(A)) + "-" + str(len(B))
	if key in memo:
		return memo[key]
	else:
		value = []
		if len(A) == 0 or len(B) == 0:
			return [""]
		elif A[-1] == B[-1]: # same last character

			value = LCS_retrieveAllString(A[:-1],B[:-1])
			value = [string + A[-1] for string in value]
		else: # different last character
			dec_A = LCS_retrieveAllString(A[:-1], B)
			dec_B = LCS_retrieveAllString(A, B[:-1])
			if len(dec_A[0]) > len(dec_B[0]):
				value = dec_A
			elif len(dec_A[0]) < len(dec_B[0]):
				value = dec_B
			elif len(dec_B[0]) == 0:
				value = dec_B
			else:
				value = dec_A + dec_B

		memo[key] = value
		return value


string_A = "ABCBDAB"
string_B = "BDCABA"

string_C = "ABBDCACB"
print (LCS_retrieveAllString(string_C, string_C[::-1]))

