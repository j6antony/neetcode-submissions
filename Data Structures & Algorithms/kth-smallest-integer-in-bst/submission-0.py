# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = self.helper(root);
        print(array);
        return array[k - 1];
        
    def helper(self, root) ->List[int]:
        if not root:
            return [];
        else:
            return self.helper(root.left) + [root.val] + self.helper(root.right);
                 
