
class Solution:
    
    
    def binarySearch(self, array, num):
        start = 0
        end = len(array)
        # print("checking",num, array)
        while start <= end:
            mid = start + (end - start) // 2
            # print(start,end, mid)
            if array[mid] >= num:
                if mid == 0 or array[mid - 1] < num:
                    array[mid] = min(array[mid], num)
                    break
                end = mid - 1
            else: # array[mid] < num
                if mid + 1 == len(array):
                    array.append(num)
                    break
                elif array[mid+1] > num:
                    array[mid+1] =  min(array[mid+1],num)
                    break
                start = mid + 1

    
    
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        running_array = [sys.maxsize]
        for i in nums:
            self.binarySearch(running_array, i)
        return len(running_array)
        
        