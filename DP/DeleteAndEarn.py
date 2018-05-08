class Solution:
    

        
    
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freqDict = dict()
        for i in nums:
            if i not in freqDict:
                freqDict[i] = 0
            freqDict[i] += 1
        sortedList = sorted(list(freqDict.keys()))
        
        # print(sortedList)
        # print(freqDict)        
        savedHash = dict()
        def recur_solve(n, obmitted):
            if n >= len(sortedList):
                return 0
            key = str(n) + str(obmitted)
            if key  in savedHash:
                return savedHash[key]          
            total = 0
            if n + 1 >= len(sortedList): # last element: just add it
                if not obmitted:
                    total += freqDict[sortedList[n]] * sortedList[n]
            else: # there is a next element
                if obmitted: # move on and not choose
                    total += recur_solve(n+1, False)
                else:
                    thisSum = freqDict[sortedList[n]] * sortedList[n]
                    if sortedList[n+1] != sortedList[n] + 1: #normal case
                        total += thisSum + recur_solve(n+1, False)
                        # print("reach")
                    else: # next element greater than 1
                        total += max(recur_solve(n+1,False), thisSum + recur_solve(n+1, True))
                        # print("not choose current ",n+1, recur_solve(n+1,False))
                        # print("choose current", n+1, thisSum + recur_solve(n+1, True))

            savedHash[key] = total
            return total
                    
        ans = recur_solve( 0, False)
        print(savedHash)

        return ans