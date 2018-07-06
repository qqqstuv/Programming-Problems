#https://leetcode.com/problems/longest-mountain-in-array/description/
#Interesting prolem
class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        max_length = 0
        up_length = 1
        down_length = 0
        last = A[0]
        last_length = 0
        
        for i in A[1:]:
            if i > last:
                up_length += 1
                
            elif i < last: # going down
                
                if up_length > 1:
                    last_length = up_length
                    down_length = 1
                    up_length = 1
                    if last_length + down_length > max_length:
                        print(i,last)
                    max_length = max(max_length, last_length + down_length) # guarantee to be 3
                else:
                    down_length += 1
                    if last_length != 0:
                        if last_length + down_length > max_length:
                            print(i,last)                        
                        max_length = max(max_length, last_length + down_length)
            else:
                up_length = 1
                down_length = 0
                last_length = 0
                    
            last = i
        print(max_length)
        return max_length