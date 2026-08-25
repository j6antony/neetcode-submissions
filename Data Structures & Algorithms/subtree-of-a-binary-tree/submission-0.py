# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True;
        elif root is None:
            return False;
        elif self.isSameTree(root, subRoot):
            return True;
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSameTree(self, root, subRoot):
        if not subRoot and not root:
            return True;
        elif not subRoot or not root or root.val != subRoot.val:
            return False;
        else:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right);


    


        

        