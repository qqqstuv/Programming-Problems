#https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
class Solution:
    def decrement(self, hm, num):
        if hm[num] > 1:
            hm[num] -= 1 
        else:
            del hm[num]
        
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.memo = dict()
        hashMap = dict()
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 0
            hashMap[i] += 1
        freq = dict()
        for num in nums:
            if num not in hashMap:
                continue
            # print(num, freq,hashMap)
            if num - 1 in freq:
                if num not in freq:
                    freq[num] = 0
                freq[num] += 1
                self.decrement(freq, num  - 1)
                self.decrement(hashMap, num)
                                
            elif num + 1 in hashMap and num + 2 in hashMap:
                if num + 2 not in freq:
                    freq[num + 2] = 0
                freq[num + 2] += 1
                self.decrement(hashMap, num)
                self.decrement(hashMap, num + 1)
                self.decrement(hashMap, num + 2)
            else:
                return False
        return True
    