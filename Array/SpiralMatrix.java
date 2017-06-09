// Spiral Matrix: print matrix in spiral
// Approach: Typical approach. 2 pointers
// Source : https://leetcode.com/problems/spiral-matrix/#/description
public class Solution {
    private int[][] matrix;
    private int length;
    private int width;
    private int order = 0;
    private int startX = 0;
    private int startY = 0;
    
    private List<Integer> getLine(int realOrder){
        List<Integer> line = new ArrayList<Integer>();
        if(length == startY || width == startX){
            return line;
        }
        if (realOrder == 0){ // go right
            for(int i = this.startX; i < this.width; i ++){
                System.out.println("right" + this.matrix[this.startY][i]);
                line.add(this.matrix[this.startY][i]);
            }
            this.startY ++;
        }else if (realOrder == 1){ // go down
            int temp = this.startX;
            this.startX = this.width - 1;
            for(int i = this.startY; i < this.length; i ++){
                System.out.println("down" + this.matrix[i][this.startX]);
                line.add(this.matrix[i][this.startX]);
            }
            this.width --;
            this.startX = temp;
        }else if(realOrder == 2){ // go left
            int temp = this.startY;
            this.startY = this.length - 1;
            for(int i = this.width - 1; i >= this.startX; i --){
                System.out.println("left" + this.matrix[this.startY][i]);
                line.add(this.matrix[this.startY][i]);
            }
            this.length --;
            this.startY = temp;
        }else if(realOrder == 3){ // go up
            for(int i = this.length - 1; i >= this.startY; i --){
                System.out.println("up" + this.matrix[i][this.startX]);
                line.add(this.matrix[i][this.startX]);
            }
            this.startX ++;
        }
        return line;
    }
    
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> answer = new ArrayList<Integer>();
        this.matrix = matrix;
        this.order = 0;
        this.length = matrix.length;
        if (length == 0) return answer;
        this.width = matrix[0].length;
        this.startX = 0;
        this.startY = 0;
        while(length != startY && width != startX){
            int realOrder = order % 4;
            answer.addAll(this.getLine(realOrder));
            order ++;
        }
        return answer;
    }
}
