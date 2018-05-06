import sys
def solve(input, index, N):
	if index >= len(input):
		return 0
	localMax = 0
	totalSum = sys.maxsize 
	for i in range(index, min(index + N, len(input))):
		localMax = max(input[i], localMax)
		remainingSum = solve(input, i + 1, N)
		totalSum = min(localMax + remainingSum, totalSum)
	return totalSum


input = [5,4,4,1,5,5,4,5,5,4,4,3,2,4,5,6,3,3,2,4,5,4,6,4,4]
N = 3


totalSum = solve(input, 0, N)

print(totalSum)