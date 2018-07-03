class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
            return 0
        if len(s) == len(t):
            return 1 if s == t else 0
        if len(t) == 1:
            return sum(i == t[0] for i in s)

        array = [[] for i in range(len(t))]
        hashDict = dict()
        for i in range(len(s)):
            if s[i] not in hashDict:
                hashDict[s[i]] = []
            hashDict[s[i]].append(i)
        for i in range(len(t)):
            if t[i] not in hashDict:
                return 0
            array[i] = hashDict[t[i]]
        temp_array = []
        
        for i in reversed(range(len(t) -  1)):
            new_temp_array = [0 for i in range(len(array[i]))]
            if not temp_array:
                temp_array = [i+1 for i in reversed(range(len(array[i+1])))] # 4 3 2 1
            idx_1 = 0
            idx_2 = 0
            array_cur = array[i]
            array_next = array[i+1]
            while idx_1 < len(array_cur):
                while idx_2 < len(array_next) and array_cur[idx_1] >= array_next[idx_2]:
                    idx_2 += 1
                if idx_2 < len(array_next):
                    new_temp_array[idx_1] += temp_array[idx_2]
                else:
                    break
                idx_1 += 1
            running_sum = 0
            for i in reversed(range(len(new_temp_array))):
                new_temp_array[i] += running_sum
                running_sum += new_temp_array[i] - running_sum
            temp_array = new_temp_array
        return temp_array[0]
            
# print(Solution().numDistinct("rabbbit", "rabbit"))