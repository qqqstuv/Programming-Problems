# Generate something like this: 
# Source: https://leetcode.com/problems/pascals-triangle/#/description
# Topics: @Array
"""
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        
        if numRows == 0:
            return result
        result.append([1])
        if numRows == 1:
            return result
        result.append([1,1])
        if numRows == 2:
            return result
        for i in range(2, numRows):
            row = [1]
            for j in range(0, len(result[-1]) - 1):
                row.append(result[-1][j] + result[-1][j + 1])
            row.append(1)
            result.append(row)
        return result
        
