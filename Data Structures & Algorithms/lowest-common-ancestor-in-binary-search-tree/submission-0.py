# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # no need to cover equality case as it is said that it wont happen in constraints
        if p.val < q.val:
            return self.helper(root, p, q);
        else:
            return self.helper(root, q, p);
    #notice in helper it will always be written so that p < q;
    def helper(self, root, p, q):
        if root == p:
            return p;
        elif root == q:
            return q;
        elif root.val > p.val and root.val < q.val:
            return root;
        elif root.val > p.val and root.val > q.val:
            return self.helper(root.left, p, q);
        else:
            return self.helper(root.right, p, q);

    
        