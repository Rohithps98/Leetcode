class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def ismagic(square):
            vals = [square[i][j] for i in range(3) for j in range(3)]
            if sorted(vals) != list(range(1,10)):
                return False
            if sum(square[0])==sum(square[1])==sum(square[1])==sum(square[i][0] for i in range(3))==sum(square[i][1] for i in range(3))==sum(square[i][2] for i in range(3))==sum(square[i][i] for i in range(3))==sum(square[i][2-i] for i in range(3))==15:
                return True
            return False
        count = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row-2):
            for j in range(col-2):
                if ismagic([grid[i+k][j:j+3] for k in range(3)]):
                    count+=1
        return count