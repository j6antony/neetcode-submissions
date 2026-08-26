# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        queue = collections.deque();
        queue.append(root);
        while queue:
            LEN = len(queue);
            level = []
            for _ in range(LEN):
                node = queue.popleft();
                if node:
                    level.append(node.val);
                    queue.append(node.left);
                    queue.append(node.right);
            if level:
                output.append(level);
        return output;


