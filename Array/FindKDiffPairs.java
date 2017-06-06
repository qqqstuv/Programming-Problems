// https://leetcode.com/problems/k-diff-pairs-in-an-array/#/description

public class Solution {
    public int findPairs(int[] nums, int h) {
        int[] temp = {2,3,4,4,5};
        if(h < 0){
            return 0;
        }else if (h == 0){
            HashMap<Integer,Integer> hm = new HashMap<Integer, Integer>();
            int preCount = 0;
            for(int i = 0; i < nums.length; i++){
                if(hm.containsKey(nums[i])){
                    int r = hm.get(nums[i]);
                    if (r == -1){
                        hm.put(nums[i], 1);
                        preCount ++;
                    }
                }else{
                    hm.put(nums[i], -1);
                }
            }
            return preCount;
        }
        ArrayList<Integer> newNums = new ArrayList<Integer>();
        for (int index = 0; index < nums.length; index++){
            newNums.add(nums[index]);
        }
        Set<Integer> hs = new HashSet<>();
        hs.addAll(newNums);
        newNums.clear();
        newNums.addAll(hs);
        nums = new int[newNums.size()];
        for(int k = 0; k < newNums.size(); k++){
            nums[k] = newNums.get(k);
        }
        int count = traverse(nums, h);
        
        return count;
    }
    
    private int traverse(int[] nums, int diff){
        int count = 0;
        for(int start = 0; start < nums.length; start ++){ // use @start to loop through the rest
            Boolean up = false;
            Boolean down = false;
            for(int k = start + 1; k < nums.length; k++){
                if (up && down) break;
                if ((nums[k] - nums[start] == diff) && !up){
                    // System.out.println(nums[start] + " " + nums[k]);
                    up = true;
                    count ++;
                }else if ((nums[k] - nums[start] == -diff ) && !down){
                    // System.out.println(nums[start] + " " + nums[k]);
                    down = true;
                    count ++;
                }
            }
        }
        return count;
    }
}