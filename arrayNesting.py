class Solution:
    def arrayNesting(self, nums):
        result = 0
        cachedResult = dict()
        for i in range(0, len(nums)):
            visited = dict()
            visited[i] = True
            length = self.recur(nums, i, 0, visited, cachedResult)
            cachedResult[i] = length # cache
            result = max(length, result)
        return result        
    
    def recur(self, nums, i, count, visited, cachedResult):
        val = nums[i]
        if cachedResult.get(val): # if the received value is already cached
            return cachedResult[val]
        else:
            if visited.get(val): # if visit a node that is already visited
                return count + 1
            else:
                visited[val] = True
                count += 1
                return self.recur(nums, val, count, visited, cachedResult)
