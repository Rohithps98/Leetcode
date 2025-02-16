class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        len = 2*(n-1)+1
        res = [0]*len
        used = set()
        def backtrack(pos):
            if pos>=len:
                return True
            if res[pos]!=0:
                return backtrack(pos+1)
            for i in range(n,0,-1):
                if i in used:
                    continue
                if i==1:
                    if pos>=len:
                        return False
                    res[pos]=1
                    used.add(1)
                    if backtrack(pos+1):
                        return True
                    res[pos] = 0
                    used.remove(1)
                else:
                    if pos+i>=len or res[pos+i]!=0:
                        continue
                    res[pos] = i
                    res[pos+i] = i
                    used.add(i)
                    if backtrack(pos+1):
                        return True
                    res[pos] = 0
                    res[pos+i] = 0
                    used.remove(i)
            return False
        backtrack(0)
        return res