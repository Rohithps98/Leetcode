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
            mid = (l+r)//2
            if matrix[bet][mid]==target:
                return True
            elif matrix[bet][mid]<target:
                l = mid+1
            else:
                r = mid-1
        return False