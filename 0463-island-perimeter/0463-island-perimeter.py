class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ro,co = len(grid),len(grid[0])
        peri = 0
        def dfs(r,c):
            if r<0 or r>=ro or c<0 or c>=co or grid[r][c]==0:
                return 1
            if grid[r][c]==-1:
                return 0
            grid[r][c]=-1
            return dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
        for r in range(ro):
            for c in range(co):
                if grid[r][c]==1:
                    peri+=dfs(r,c)
        return peri