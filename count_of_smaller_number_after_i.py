#https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

class Solution:
    
    def binary_add(self, binary, num):
        left = 0
        right = len(binary) - 1
        idx_found = 0
        # print("searching for", num)
        while left <= right:
            mid = left + (right - left) // 2
            # print(left, right, "mid", mid, "val",binary[mid])
            
            if num <= binary[mid]  and (mid - 1 < 0 or binary[mid-1] < num):
                idx_found =  mid - 1
                # print("First case")
                break
            if binary[mid] < num and (mid + 1 >= len(binary) or num <= binary[mid+1]):
                idx_found = mid
                # print("Second case")
                break
            if binary[mid] >= num:
                right = mid - 1
            else:
                left = mid + 1
        # print("found", num, "indx",idx_found)
        idx_found =  idx_found + 1
        binary.insert(idx_found, num)
        return idx_found
        
        
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums ) == 0:
            return []
        ans = [0 for i in range(len(nums))]
        binary = []
        for idx in reversed(range(len(nums))):
            ans[idx] = self.binary_add(binary, nums[idx])
            # print(binary)
        ans[-1] = 0
        return ans
        
        