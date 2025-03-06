class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(start,val,path):
            if val==0:
                res.append(path[:])
                return
            for i in range(start,len(candidates)):
                if candidates[i]>val:
                    break
                path.append(candidates[i])
                backtrack(i,val-candidates[i],path)
                path.pop()
        backtrack(0,target,[])
        return res
