class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {};
        def dfs(row, col):
            if row == m - 1 and col == n - 1:
                return 1
            if (row, col) in dp:
                return dp[(row, col)]
            else:
                if row == m - 1:
                    dp[(row, col)] = dfs(row, col + 1)
                    return dp[(row, col)]
                elif col == n - 1:
                    dp[(row, col)] = dfs(row + 1, col)
                    return dp[(row, col)]
                dp[(row, col)] =  dfs(row+1, col) + dfs(row, col + 1)
                return dp[(row, col)]
        return dfs(0, 0)


