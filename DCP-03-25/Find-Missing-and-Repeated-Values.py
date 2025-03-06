class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n*n
        actsum = N*(N+1)//2
        seen = set()
        su = 0
        repeat = -1
        for row in grid:
            for num in row:
                su+=num
                if num in seen:
                    repeat = num
                seen.add(num)
        missing = actsum - (su-repeat)
        return [repeat,missing]