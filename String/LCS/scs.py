

memo = dict()

def SCS(A,B):
	if len(A) == 0:
		return B
	elif len(B) == 0:
		return A
	elif A[-1] == B[-1]:
		return SCS(A[:-1], B[:-1]) + A[-1]
	else: # last char different
		leftSide = SCS(A[:-1], B) + A[-1] # compute for left side
		rightSide = SCS(A, B[:-1]) + B[-1] # compute for right side
		if  len(leftSide) > len(rightSide):
			return rightSide
		else:
			return leftSide
			
string_A = "ABCBDAB"
string_B = "BDCABA"

print(SCS(string_A, string_B))