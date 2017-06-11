// Source: https://leetcode.com/contest/leetcode-weekly-contest-36/problems/valid-triangle-number/
/*
    Topics: @Array, @Math
    This is a very smart solution from a LeetCode user.
    Basically, there are three pointers. First pointers go from left to right.
    Second pointer goes from left to right, third go from righ to left
    Increment third pointer to the point where it's valid, then calculate the valid range: count += r - l
    Then decrement the second pointer and so on
*/
public class Solution {
    public static int triangleNumber(int[] A) {
        Arrays.sort(A);
        int count = 0, n = A.length;
        for (int i=n-1;i>=2;i--) {
            int l = 0, r = i-1;
            while (l < r) {
                if (A[l] + A[r] > A[i]) {
                    count += r-l;
                    r--;
                }
                else l++;
            }
        }
        return count;
    }
}
