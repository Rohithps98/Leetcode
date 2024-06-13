class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot,l,r = 0,len(matrix)-1,0,len(matrix[0])-1
        while top<=bot:
            bet = (top+bot)//2
            if matrix[bet][0]>target:
                bot = bet-1
            elif matrix[bet][-1]<target:
                top = bet+1
            else:
                break
        if not top<=bot:
            return False
        while l<=r:
            m = (l+r)//2
            if matrix[bet][m]==target:
                return True
            elif matrix[bet][m]<target:
                l=m+1
            else:
                r = m-1
        return False