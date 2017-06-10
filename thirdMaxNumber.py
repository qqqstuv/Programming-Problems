# Source: https://leetcode.com/problems/third-maximum-number/#/solutions

class Solution(object):
    def thirdMax(self, nums):
            nums = set(nums)
            if len(nums) < 3:
                return max(nums)
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)
