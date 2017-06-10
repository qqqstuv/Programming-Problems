# https://leetcode.com/problems/first-missing-positive/#/description
# Implementation: @Hash, @Array

import sys
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge case
        if len(nums) == 0:
            return 1
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            for i in range(1, nums[0]):
                return 1
      
        positiveMin = sys.maxsize
        size = len(nums) + 1
        for i in nums:
            if i < 0:
                size -= 1
            elif i < positiveMin:
                positiveMin = i
            
        hashArray = [-1 for i in range(size)]
        for i in nums:
            if i >= 0 and i <= size: #if the number is positive and is less than the size of the hashArray (we dont care about values greater than the size of the hashArray)
                hashArray[i - 1] = i
        print(hashArray)
        for idx, val in enumerate(hashArray):
            if val == -1:
                temp = idx
                while temp >= 0: # find lowerbound
                    if hashArray[temp] != -1:
                        return hashArray[temp] + idx - temp
                    temp -= 1
                temp = idx
                while temp < len(hashArray): # find in upperbound
                    if hashArray[temp] != -1:
                        print(temp)
                        return hashArray[temp] + idx - temp
                    temp += 1
                return 1    
            
        
        
