#https://leetcode.com/problems/find-peak-element/description/
class Solution:
    def isPeak(self, nums, idx):
        if idx - 1 >= 0:
            if nums[idx - 1] > nums[idx]:
                return False
        if idx + 1 < len(nums):
            if nums[idx + 1] > nums[idx]:
                return False
        # print("Peak",nums,idx, nums[idx])
        return True

    def solve(self, nums):
        mid = len(nums) // 2
        # print("Mid idx", mid,"num", nums[mid])
        if self.isPeak(nums, 0):
            return 0
        elif self.isPeak(nums, len(nums) - 1):
            return len(nums) - 1
        elif self.isPeak(nums, mid):
            return mid
        start = nums[0]
        end = nums[-1]
        if start > nums[mid]:
            return self.solve(nums[:mid])
        elif end > nums[mid]:
            return (mid + 1) + self.solve(nums[mid+1:])
        else:
            if mid -1 >= 0 and nums[mid - 1] > nums[mid]:
                return self.solve(nums[:mid])
            elif mid + 1 < len(nums) and nums[mid + 1] > nums[mid]:
                return (mid + 1) + self.solve(nums[mid+1:])
            else:
                print("error")
        
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = self.solve(nums)
        return ans