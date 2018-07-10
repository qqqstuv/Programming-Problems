#https://leetcode.com/problems/making-a-large-island/description/
class Solution:
    
    def dfs(self, i,j, grid, num):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return 0
        grid[i][j] = num
        total = 1
        total += self.dfs(i+1, j, grid, num)
        total += self.dfs(i-1, j, grid, num)
        total += self.dfs(i, j+1, grid, num)
        total += self.dfs(i, j-1, grid, num)
        return total
        
    
    def getMaxConnect(self, i,j, grid, size):
        set_island = set()
        if i + 1 < len(grid) and grid[i+1][j] < 0:
            set_island.add(grid[i+1][j])
        if i - 1 >= 0 and grid[i-1][j] < 0:
            set_island.add(grid[i-1][j])            
        if j + 1 < len(grid) and grid[i][j+1] < 0:
            set_island.add(grid[i][j+1])
        if j - 1 >= 0 and grid[i][j-1] < 0:
            set_island.add(grid[i][j-1])
        total = 1
        for island in set_island:
            total += size[island]
        # print(i,j, total, set_island)

        return total 

    
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        size = dict()
        island_idx = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    size[island_idx] = self.dfs(i,j,grid, island_idx)
                    island_idx -= 1
        # print(size)
        # for i in grid:
        #     print(i)
        ans = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    ans = max(ans, self.getMaxConnect(i,j,grid,size))
        if not size:
            return ans
        return max(ans, max(list(size.values())))