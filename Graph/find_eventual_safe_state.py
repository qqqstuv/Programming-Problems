#https://leetcode.com/problems/find-eventual-safe-states/description/
class Solution:
    
    def check(self, graph, idx, curr):
        if idx in self.circle:
            return False
        if idx in self.non_circle:
            return True
        if len(graph[idx]) == 0:
            self.non_circle.add(idx)
            return True
        else:
            ans = True
            for child in graph[idx]:
                if child in curr:
                    ans = False
                elif not self.check(graph, child, curr + [idx]):
                    ans = False
            if ans:
                self.non_circle.add(idx)
            else:
                self.circle.add(idx)

            return ans
                
            
    
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        self.circle = set()
        self.non_circle  = set()
        for idx in range(len(graph)):
            self.check(graph, idx, [])
        # print(self.circle, self.non_circle)
        return sorted(self.non_circle)
            
            