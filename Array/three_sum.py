
#Classic 3sum problem found on leetcode. Use 2 pointers to solve in O(n^2) and O(1)

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        i,j,k = 0,0,0
        ans = []
        for i in range(len(nums)-2):
            #Avoid duplicate on i
            if (i != 0 and nums[i] == nums[i-1]):
                continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    #Avoid duplicate
                    while (j < k and nums[j] == nums[j-1]):
                        j += 1

                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return ans