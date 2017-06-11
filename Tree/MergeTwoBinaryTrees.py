// Source: https://leetcode.com/contest/leetcode-weekly-contest-36/problems/merge-two-binary-trees/
/*
Merge two binary trees. Uses preOrder Traversal. Pretty simple but the coding part can be tricky
Topics: @BinaryTree, @Tree, @Traverse
*/

public class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return null;
        
        int val = (t1 == null ? 0 : t1.val) + (t2 == null ? 0 : t2.val); // Either sum of two leaf or null
        //Pre-order traversal
        TreeNode newNode = new TreeNode(val);
        newNode.left = mergeTrees(t1 == null ? null : t1.left, t2 == null ? null : t2.left);
        newNode.right = mergeTrees(t1 == null ? null : t1.right, t2 == null ? null : t2.right);
        
        return newNode;
    }
}
