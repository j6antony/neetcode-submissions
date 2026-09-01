class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        sum = 0;
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum += self.helper(grid, i, j);

        return sum

        
    def helper(self, grid, i, j):
        if i > len(grid) - 1 or i < 0 or j > len(grid[0]) - 1 or j < 0:
            return 0;
        else:
            if grid[i][j] == "1":
                grid[i][j] = "0";
                self.helper(grid, i + 1, j)
                self.helper(grid, i, j + 1)
                self.helper(grid, i - 1, j)
                self.helper(grid, i, j - 1)
                return 1 
            return 0

