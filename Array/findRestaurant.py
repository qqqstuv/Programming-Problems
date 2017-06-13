# Src: https://leetcode.com/contest/leetcode-weekly-contest-34/problems/minimum-index-sum-of-two-lists/
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hash1 = dict()
        hash2 = dict()
        # turn into hash map with key is string and value is index
        for idx, val in enumerate(list1):
            hash1[val] = idx
        for idx, val in enumerate(list2):
            hash2[val] = idx

        result = dict()
        for key, val in hash1.items():
            if key in hash2: # if match
                result[key] = hash2.get(key) + val
            else: # not match
                pass
        # print (result)
        minIndex = min(result.values())
        
        final = []
        for key, val in result.items():
            if val == minIndex:
                final.append(key)
        # print("FINAL:", final)
        return final
