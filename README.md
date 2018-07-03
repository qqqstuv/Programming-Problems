# Programming-Problem

Solutions to some programming problems found online


#### May 06, 2018
[Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/description/)
This is a review of a question I've done before so not a big deal. 
Tag: DP, String, Subsequence.


[3Sum](https://fizzbuzzed.com/top-interview-questions-1/#twopointerm)
Classic 3Sum problem. Use 2 pointers (actually 3) to solve. The solution is pretty straightforward. However need to check for 2 places where duplicates are not allowed


#### May 08, 2018

[Delete And Earn](https://leetcode.com/problems/delete-and-earn/description/)
One of the easy DP problem although it seems deceptive at first. 

#### May 23, 2018

[Best time to buy and sell stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
Given a list of ints of value of stock. You can only buy/sell once through the whole thing. Return the maximum profit.
The optimal solution of this problem is O(n). A bit tricky.

[Containter with most water](https://leetcode.com/problems/container-with-most-water/description/)
An easier version of Trapping Rain Water. Can be solved with 2 pointers in linear time with constant space. Have been asked in interview before.
Just use two pointers from left and right and move the smaller one in while updating the max water store.

[CombinationSum IV](https://leetcode.com/problems/combination-sum-iv/description/)
A variation of DP. Pretty simple and straightforward DP.

#### May 25, 2018

[Number of Islands](https://leetcode.com/problems/number-of-islands/description/)
Redid this problem. One pass.

[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)
Easy problem but very tricky with indexes

#### May 30, 2018

[Surrounded Region](https://leetcode.com/problems/surrounded-regions/description/)
Graph search problem. There is a trick. Do mutiple bfs/dfs from the side.

[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)
Seen this before. Have to do a Post Order Traversal. There are 4 cases I need to keep track of: max(root, root + left,root. right, root + left + right). 

[House Robber III](https://leetcode.com/problems/house-robber-iii/description/)
Pretty straight forward solution but a little bit tricky to implement traversal


#### May 31, 2018

Reviewed implementing QuickSort and MergeSort.

#### June 7, 2018
Review LinkedList, Palindrome in C in both recursive and iterative method

#### June 27, 2018
[Split array into consecutive subquence](https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/)
Pretty interesting problem. Could be done in O(n^2) or O(n)

[Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/)
Traverse and append to a list in vertical order. Can be solved with in order BFS, or something better!

#### June 28, 2018
[Number of subarray with bounded maximum](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/)
Interesting problem. Brute force is DP O(n^2  * logn) but there can be O(n) O(n) solution.
Snippet Code to calculate the index(start, end) of adjacent similar values.
```
A = [False, False, True, False, True, True, True, False, True]
ans = []
idx = 0
while idx < len(A):
    count = 0
    while idx < len(A) and A[idx] :
        count += 1
        idx += 1
    if count > 0:
        ans.append([idx - count, idx])
    else:
        idx += 1
print(ans)
#[[2, 3], [4, 7], [8, 9]]
```

[Find Eventual Safe Place](https://leetcode.com/problems/find-eventual-safe-states/description/)
Pretty straight forward graph problem. Can be done in O(n) by implementing a simple finding circle in graph algorithm

[Find all duplicates in array](https://leetcode.com/problems/find-all-duplicates-in-an-array/description/)
Very tricky problem. Solution is not bitshifting but playing around with array from 1 to n

[Partition Label](https://leetcode.com/problems/partition-labels/description/)
Can be solved by DP O(n^2) brute force way but can also be done in  O(n), O(n). Think differently.

#### June 29, 2018

How to check if a singly linkedList is palindromic using recursion with 1 traversal and constant space:

```
bool recursiveCheck(ListNode* right, ListNode** left){
	if (right != NULL){
		if (recursiveCheck(right->next, left)){
			if (right->val == (*left)->val){
				(*left) = (*left)->next;
				return true; 	
			}else{
				return false;
			}	
		}else{
			return false;
		}
	}
	return true;
}
bool isRecursive(ListNode* head){
	ListNode* node = head;
	return recursiveCheck(head, &node);
}
``` 

#### July 2, 2018

[Verify Preorder Serialization of a Binary Tree](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/)
Can do stack or can do with regex. Good medium problem