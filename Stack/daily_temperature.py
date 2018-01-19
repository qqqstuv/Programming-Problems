#https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = []
        stack.append([temperatures[0], 0])
        
        for i in range(1, len(temperatures)):
            if len(stack) != 0:
                last = stack[-1]
                while last[0] < temperatures[i]:
                    result[last[1]] =  i - last[1]  # set index
                    stack.pop()
                    if len(stack) == 0:
                        break
                    last = stack[-1]
                stack.append([temperatures[i], i])
        return (result)