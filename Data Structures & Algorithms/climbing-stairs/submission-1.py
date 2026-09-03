class Solution:
    def climbStairs(self, n: int) -> int:
        map = {}
        
   
        def dfs (target, cur: int):
            if cur > target:
                return 0
            elif cur == target:
                return 1
            else:
                if cur in map:
                    return map[cur]
                ans = dfs(target, (cur+1)) + dfs(target, (cur + 2))
                map[cur] = ans
                return ans
        return dfs(n, 0)