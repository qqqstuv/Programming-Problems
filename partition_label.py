#https://leetcode.com/problems/partition-labels/description/
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        hm = dict()
        for idx in range(len(S)):
            hm[S[idx]] = idx
        # print(hm)
        i = 0
        stop = 0
        ans = []
        while(i < len(S)):
            letter = S[i]
            start = i
            stop = hm[letter]
            while(i < stop):
                i += 1
                letter = S[i]
                if hm[letter] > stop:
                    stop = hm[letter]
            # print(stop, start)
            ans.append(stop - start + 1)
            i = stop + 1
        # print(ans)
        return (ans)
                
                
            
                