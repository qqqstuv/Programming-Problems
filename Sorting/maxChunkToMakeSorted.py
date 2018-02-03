# https://leetcode.com/problems/max-chunks-to-make-sorted/description/#
class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        offset = [0] * len(arr)
        for idx in range(len(arr)):
            offset[idx] = arr[idx] - idx
        curSum = 0
        i = 0
        while i < len(arr):
            curSum += offset[i]
            if curSum == 0:
                count += 1
                curSum = 0
            i += 1
        return count