# https://leetcode.com/contest/leetcode-weekly-contest-35/problems/can-place-flowers/

class Solution:
    def getCount(self, start, end):
        print(start, end)
        space = int(((end - start - 1) - 1) / 2)
        print("result",space)
        if space < 0:
            return 0
        return space
    
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        else:
            count = 0
            start = 0
            if flowerbed[0] == 0:
                flowerbed = [1,0] + flowerbed
            if flowerbed[-1] == 0:
                flowerbed = flowerbed + [0,1]
            for idx, val in enumerate(flowerbed):
                if val == 1:
                    count += self.getCount(start, idx)
                    start = idx
            print ("count",count)
            if count >= n:
                return True
            else:
                return False
                    
        
        
