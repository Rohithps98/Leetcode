class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy = []
        def backtrack(curr):
            if len(curr) == n:
                happy.append(curr)
                return len(happy) == k
            for ch in 'abc':
                if not curr or curr[-1]!=ch:
                    if backtrack(curr+ch):
                        return True
        backtrack("")
        return happy[k-1] if k<=len(happy) else ""