class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        comp = 0
        visited = set()
        def dfs(last, i):
            if i in visited:
                return
            visited.add(i)
            for n in adj[i]:
                if n != i:
                    dfs(i, n)
            
        for i in range(n):
            if i not in visited:
                dfs(-1, i)
                comp+= 1
        return comp
        
    
        
