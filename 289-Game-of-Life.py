class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        \\\
        Do not return anything, modify board in-place instead.
        \\\
        if not board or not board[0]:
            return
        ro,co = len(board),len(board[0])
        def count(row,col):
            count = 0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if dr==0 and dc==0:
                        continue
                    r = row+dr
                    c = col+dc
                    if 0<=r<ro and 0<=c<co and board[r][c]==1:
                        count+=1
            return count
        changes = []
        for r in range(ro):
            for c in range(co):
                liven = count(r,c)
                if board[r][c]==1:
                    if liven<2 or liven>3:
                        changes.append((r,c,0))
                else:
                    if liven==3:
                        changes.append((r,c,1))
        for r,c,new in changes:
            board[r][c]=new