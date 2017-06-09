# Source: https://leetcode.com/problems/missing-number/#/description:

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expected = len(nums) *(len(nums) + 1 ) / 2
        print (expected, len(nums))
        realtiy = 0
        for i in nums:
            realtiy += int(i)
        num = expected - realtiy
        return num