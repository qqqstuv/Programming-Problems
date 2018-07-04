#https://leetcode.com/problems/combination-sum/description/
class Solution:
    
    def recur(self, current, candidates, so_far, last_idx):
        if current == self.target:
            self.ans.append(so_far)
            return
        elif current > self.target:
            return
        else:
            for idx in range(last_idx, len(candidates)):
                self.recur(current + candidates[idx], candidates, so_far + [candidates[idx]], idx)
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.target = target
        self.ans =  []
        self.recur(0,candidates, [], 0)
        return self.ans
        