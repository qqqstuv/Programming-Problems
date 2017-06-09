// https://leetcode.com/problems/rotate-image/#/solutions
// IDEA: first transpose the matrix, then flip it horizontally

/*
1 2 3
4 5 6
7 8 9
transpose:
1 4 6
2 5 8
3 6 9
flip:
7 4 1
8 5 2
9 6 3

*/
public class Solution {
    public void rotate(int[][] matrix) {
        for(int i = 0; i<matrix.length; i++){
            for(int j = i; j<matrix[0].length; j++){
                int temp = 0;
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for(int i =0 ; i<matrix.length; i++){
            for(int j = 0; j<matrix.length/2; j++){
                int temp = 0;
                temp = matrix[i][j];
                matrix[i][j] = matrix[i][matrix.length-1-j];
                matrix[i][matrix.length-1-j] = temp;
            }
        }
    }
}
