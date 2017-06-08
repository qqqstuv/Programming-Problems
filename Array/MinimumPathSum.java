import java.util.Queue;
import java.util.LinkedList;

// Source: https://leetcode.com/problems/minimum-path-sum/#/description
// Approach: Implement Dijkstra with a queue to find a path from top to bottom. Treat the grid as an actual graph
// This is just a pseudo solution. Complele solution is in the python file

public class Solution {
    
    public class Input {
        public int[][] grid;
        public int length;
        public int width;
        public void Input(int[][] grid){
            this.grid = grid;
            this.length = grid.length;
            this.width = grid[0].length;
        }
        public LinkedList<LinkedList<Integer>> neighbors(LinkedList<Integer> coord){
            LinkedList<LinkedList<Integer>> neighbors = new LinkedList<LinkedList<Integer>>();
            if (coord.get(0) + 1 < this.length){
                neighbors.add(new LinkedList<Integer>(Arrays.asList(coord.get(0) + 1, coord.get(1))));
            }
            if(coord.get(1) + 1 < this.width){
                neighbors.add(new LinkedList<Integer>(Arrays.asList(coord.get(0), coord.get(1) + 1)));
            }
            return neighbors;
        }
    }
    public int minPathSum(int[][] origin) {
        if(origin.length == 1 && origin[0].length == 1){
            return origin[0][0];
        }
        
        Queue<Integer> queue = new LinkedList<>();
        Input input = new Input(origin);
        queue.add(origin[0][0]);
        int[][] best = new int[input.length][input.width];
        for(int i=0; i<input.length; i++) {
            for(int j=0; j<input.width; j++) {
                best[i][j] = Integer.MAX_VALUE;
            }
        }
        
        while (queue.size() != 0){
            LinkedList<Integer> node = queue.remove();
            LinkedList<LinkedList<Integer>> neighbors = input.neighbors(node);
            for(LinkedList<Integer> neighbor : neighbors){
                int current = best[neighbor.get(0)][neighbor.get(1)];
                int parent = best[node.get(0)][node.get(1)];
                int nodeVal = origin[neighbor.get(0)][neighbor.get(1)];
                int newVal = parent + nodeVal;
                if (parent + nodeVal > current){ //reset
                    newVal = current;
                }
                best[neighbor.get(0)][neighbor.get(1)] = newVal;
                queue.add(neighbor);
            }
            return best[input.length - 1][input.wdith -1];
        }
    }
}
