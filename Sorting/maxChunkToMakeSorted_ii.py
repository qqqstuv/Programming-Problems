# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/description/

import sys, copy
class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sortArray = copy.deepcopy(arr)
        sortArray.sort()
        range_dict = dict()
        for idx in range(len(sortArray)):
            if sortArray[idx] not in range_dict:
                range_dict[sortArray[idx]] = []
            range_dict[sortArray[idx]].append(idx)
        indexArray = [0] * len(arr)
        for idx in range(len(arr)):
            indexArray[idx] = range_dict[arr[idx]][0] - idx
            range_dict[arr[idx]].pop(0)
        count = 0
        array_sum = 0
        i = 0
        while i < len(indexArray):
            array_sum += indexArray[i]
            if array_sum == 0:
                count += 1
                array_sum = 0
            i += 1
        return count