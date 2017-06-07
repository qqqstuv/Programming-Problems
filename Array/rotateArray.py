# https://leetcode.com/problems/rotate-array/#/description
class Solution(object):
    
    def reverse(self,nums, start, end):
        
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end   -= 1
        print(nums)
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0,len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums,0, len(nums) -1 )