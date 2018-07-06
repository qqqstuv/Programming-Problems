#https://leetcode.com/problems/binary-trees-with-factors/description/
#Interesting binary tree, or permutation problem.
class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        hashDict = dict()
        nums = set(A)
        for num in A:
            hashDict[num] = 1
        A =sorted(A)
        print(A)
        for i in range(len(A)):
            for j in range(0, i):
                key = A[i] / A[j]                
                if int(key) == key and key in nums:
                    child_permutation = hashDict[A[j]] * hashDict[key]
                    hashDict[A[i]] += child_permutation
        # for i in sorted(list(hashDict.keys())):
        #     print(i, hashDict[i])
        print(hashDict)
        total = sum(list(hashDict.values())) % (10 ** 9 + 7)
        return total
                    
                    