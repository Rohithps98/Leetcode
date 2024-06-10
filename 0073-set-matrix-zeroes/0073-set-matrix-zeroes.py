class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c = len(matrix),len(matrix[0])
        a,b = [0]*r,[0]*c
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    a[i]=1
                    b[j]=1
        for i in range(r):
            for j in range(c):
                if a[i] or b[j]:
                    matrix[i][j]=0