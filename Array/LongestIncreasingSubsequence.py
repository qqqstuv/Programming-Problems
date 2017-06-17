# My solution to: https://www.techiedelight.com/longest-increasing-subsequence-using-dynamic-programming/
# O(n^2), O(n)
if __name__ == '__main__':
	arr = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
	# print(arr)
	memoization = [[0, -1] for i in range(len(arr))]
	for i in reversed(range(0, len(arr))):
		localMax = [0,0]
		for j in range(i, len(arr)):
			if arr[i] < arr[j]:
				if memoization[j][0] > localMax[0]:
					localMax[0] = memoization[j][0] # length of LIS
					localMax[1] = j # index chosen
		# print(arr[i], localMax)
		memoization[i][0] = localMax[0] + 1
		memoization[i][1] = localMax[1]
	# print(memoization)

	absoluteMax = 0
	idx = 0
	for i in range(len(memoization)):
		if memoization[i][0] > absoluteMax:
			absoluteMax = memoization[i][0]
			idx = i
	print(arr[idx])
	while 1:
		idx = memoization[idx][1]
		print(arr[idx])
		if idx == len(arr) - 1:
			break
