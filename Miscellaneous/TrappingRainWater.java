// Source: https://leetcode.com/problems/trapping-rain-water/#/description
/*
Implementation: @2Pointers
Use two pointers from left and right to keep track of leftMin and rightMin
Because it comes from left and right, the middle bars are guaranteed to be covered by the boundary.
Iterate from both sides and calculate the water stored on the fly
*/
public class Solution {
    public int trap(int[] A){
        int a=0;
        int b=A.length-1;
        int max=0;
        int leftmax=0;
        int rightmax=0;
        while(a<=b){
            leftmax=Math.max(leftmax,A[a]);
            rightmax=Math.max(rightmax,A[b]);
            if(leftmax<rightmax){
                max+=(leftmax-A[a]);       // leftmax is smaller than rightmax, so the (leftmax-A[a]) water can be stored
                a++;
            }
            else{
                max+=(rightmax-A[b]);
                b--;
            }
        }
        return max;
    }
}
