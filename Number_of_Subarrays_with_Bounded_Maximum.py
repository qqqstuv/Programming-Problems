#https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/
class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        partition_array = [False] * len(A)
        for i in range(len(A)):
            if A[i] > R:
                partition_array[i] = True
        
        def solve_partitioned_array(array):
            partition_less_than = [False] * len(array)
            for i in range(len(array)):
                if array[i] < L:
                    partition_less_than[i] = True
            # print(partition_less_than)

            total = len(array) * (len(array) + 1) // 2
            index = 0
            less_than_permute_count = []
            while index < len(partition_less_than):
                count = 0
                while index < len(partition_less_than) and partition_less_than[index]:
                    count += 1
                    index += 1
                if count > 0:
                    less_than_permute_count.append(count)
                else:
                    index += 1
            # decrease the less than permutation cost
            for count in less_than_permute_count:
                total -= count * (count + 1) // 2
            return total
        idx = 0
        Ans = 0
        # print(partition_array)
        while idx < len(partition_array):
            count = 0
            while idx < len(partition_array) and not partition_array[idx] :
                count += 1
                idx += 1
            if count > 0:
                # print(idx-count, idx, A[idx - count: idx])
                Ans  += solve_partitioned_array(A[idx - count: idx])
            else:
                idx += 1
        return Ans
                
            