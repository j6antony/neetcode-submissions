"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node];
            else:
                newNode = Node()
                oldToNew[node] = newNode;
                newNode.val = node.val
                for i in node.neighbors:
                    newNode.neighbors.append(dfs(i))
                return newNode;
                
        if node:
            return dfs(node)
        