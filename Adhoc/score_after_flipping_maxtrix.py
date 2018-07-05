#https://leetcode.com/problems/score-after-flipping-matrix/description/
class Solution:
    
    def flip_row(self, A, row):
        A[row] = [0 if i == 1 else 1 for i in A[row]]
        
    def print_A(self, A):
        for i in A:
            print(i)
            
    def flip_column(self, A, col):
        
        for i in range(len(A)):
            A[i][col] = 1 if A[i][col] == 0 else 0
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(len(A)):
            if A[i][0] == 0:
                self.flip_row(A, i)
        self.print_A(A)
        for j in range(1, len(A[0])):
            zero_count = 0
            for k in range(len(A)):
                if A[k][j] == 0:
                    zero_count += 1
            # print(zero_count)
            if len(A) - zero_count < zero_count:
                print("flip")
                self.flip_column(A, j)
            self.print_A(A)
        # print(A)
        total = 0
        for row in A:
            total += int(''.join(str(x) for x in row),2)
            # print(total)
        return total
                