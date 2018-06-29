class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def dfs(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y]:
                grid[x][y] = 0
                return 1 + dfs(x + 1, y) + dfs(x, y + 1) + dfs(x - 1, y) + dfs(x, y - 1)
            return 0

        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    area = max(area, dfs(i, j))
        
        return area

island1 = [ [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0] ]
island2 = [[0,0,0,0,0,0,0,0]]

print Solution().maxAreaOfIsland(island1)
print Solution().maxAreaOfIsland(island2)