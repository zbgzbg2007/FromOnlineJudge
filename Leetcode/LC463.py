class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i-1 < 0 or grid[i-1][j] == 0:
                        ans += 1
                    if i+1 >= n or grid[i+1][j] == 0:
                        ans += 1
                    if j-1 < 0 or grid[i][j-1] == 0:
                        ans += 1
                    if j+1 >= m or grid[i][j+1] == 0:
                        ans += 1
        return ans
