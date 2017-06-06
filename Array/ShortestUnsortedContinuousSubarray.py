# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
# You need to find the shortest such subarray and output its length

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

import sys
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = [2,6,4,8,10,9,15]
        includeIndex = None
        max = -sys.maxsize
        start = -1
        end = -1
        length = len(nums) - 1
        for idx, val in enumerate(nums):
            if val >= max:
                max = val
                # if idx == length and start != -1:
                #     end = idx
            else: # val < max (lower)
                # print("lower value",val, idx)
                end = idx
                if start == -1:
                    start = idx
                    for i in range(0, start):
                        if nums[i] > val:
                            start = i
                            break
                else:
                    for i in range(0, start + 1):
                        if nums[i] > val:
                            start = i
                            break
        # print(start, end)
        if start == -1:
            return 0
        elif start == 0:
            return end - start + 1
        else:
            return end - start + 1