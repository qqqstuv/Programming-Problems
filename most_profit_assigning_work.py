#https://leetcode.com/problems/most-profit-assigning-work/description/
class Solution:
    
    def binarySearch(self, profits, worker):
        start = 0
        end = len(profits) -1
        # print(profits, worker)
        while(start <= end):
            mid = start + (end - start) // 2
            # print(start,mid,end,profits[mid][0])
            if profits[mid][0] < worker:
                if mid + 1 == len(profits) or profits[mid+1][0] > worker:
                    return profits[mid][1]
                start = mid + 1
            elif profits[mid][0] > worker:
                if mid - 1 < 0:
                    return 0
                elif profits[mid-1][0] < worker:
                    return profits[mid-1][1]
                end  = mid - 1
            else:
                return profits[mid][1]
        return -1
    
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        profits = []
        for i in range(len(profit)):
            profits.append([difficulty[i], profit[i]])
        profits = sorted(profits, key = lambda x : x[1])
        cur_max = sys.maxsize
        distinct_profit = []
        for idx in reversed(range(len(profits))):
            if profits[idx][0] < cur_max:
                distinct_profit.insert(0,[profits[idx][0], profits[idx][1]])
            cur_max = min(cur_max, profits[idx][0])
        print(distinct_profit)
        ans = [self.binarySearch(distinct_profit, eachWorker) for eachWorker in worker]
        return sum(ans)
            