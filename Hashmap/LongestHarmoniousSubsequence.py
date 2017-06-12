# Source: https://leetcode.com/problems/longest-harmonious-subsequence/#/description
# Topics: @Hashmap, @Array
import sys
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        hashTable = dict()
        for i in nums:
            if not hashTable.get(i):
                hashTable[i] = 0
            hashTable[i] += 1
        
        a = hashTable.keys()
        # print(a)
        sortedList = list(map(int, a))
        sortedList.sort()
        # print(sortedList)
        maxSize = - sys.maxsize
        modified = False
        for i in range(0, len(sortedList) - 1):
            # print(sortedList[i], sortedList[i+1], hashTable[sortedList[i]], hashTable[sortedList[i + 1]])
            if sortedList[i + 1] - sortedList[i] == 1 and hashTable[sortedList[i]] + hashTable[sortedList[i + 1]] > maxSize:
                maxSize = hashTable[sortedList[i]] + hashTable[sortedList[i + 1]]
                modified = True
        return maxSize if modified else 0
