#https://leetcode.com/problems/max-points-on-a-line/description/
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:

    def check(self, arr):
        
        hashMap = dict()
        same_coordinates = 0
        for x,y in arr:
            # print(x,y)
            if y == 0:
                if x == 0:
                    same_coordinates += 1
                else:
                    if "0" not in hashMap:
                        hashMap["0"] = 0
                    hashMap["0"] += 1
            else:
                if x / y not in hashMap:
                    hashMap[x/y] = 0
                hashMap[x/y] += 1
        if not hashMap:
            return same_coordinates
        # print(max(list(hashMap.values())),same_coordinates)
        
        return max(list(hashMap.values())) + same_coordinates
            
    
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        ans = 0
        for idx in range(len(points)):
            offset = points[idx]
            
            _max = self.check([i.x - offset.x, i.y - offset.y] for i in points[:idx] + points[idx+1:])
            # print(_max)
            ans = max(ans, _max + 1)
        return ans 
