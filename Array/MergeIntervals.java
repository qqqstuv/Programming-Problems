// Source: https://leetcode.com/problems/merge-intervals/#/solutions
// Use two arrays start and end, sort both the list and merge them. Kinda weird. Gotta check back on this

/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        int size = intervals.size();
        int[] starts = new int[size];
        int[] ends = new int[size];
    	for (int i = 0; i < size; i++) {
    		starts[i] = intervals.get(i).start;
    		ends[i] = intervals.get(i).end;
    	}
    	Arrays.sort(starts);
    	Arrays.sort(ends);
    	// loop through
    	List<Interval> res = new ArrayList<Interval>();
    	for (int i = 0, j = 0; i < size; i++) { // j is start of interval.
    		if (i == size - 1 || starts[i + 1] > ends[i]) {
    			res.add(new Interval(starts[j], ends[i]));
    			j = i + 1;
    		}
    	}
    	return res;
    }
}
