// Source: https://leetcode.com/problems/sort-colors/#/description
// Sort colors 0 1 2 in one pass. Smart solution
class Solution {
    public void sortColors(int A[], int n) {
            int second=n-1, zero=0;
            for (int i=0; i<=second; i++) {
                while (A[i]==2 && i<second) swap(A[i], A[second--]);
                while (A[i]==0 && i>zero) swap(A[i], A[zero++]);
            }
    }
}