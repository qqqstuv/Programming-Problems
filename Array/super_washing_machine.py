class Solution:
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        same = sum(machines) / len(machines)
        if int(same) != same:
            return -1
        curr_max = 0
        curr_offset = 0
        addOne = False
        for idx in range(len(machines)):
            idx_offset = machines[idx] - same
            prev_offset = curr_offset
            curr_offset += idx_offset  
            curr_max = max(curr_max, abs(curr_offset),idx_offset)
        return int(curr_max)