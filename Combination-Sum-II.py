class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(pos,cur,target):
            if target==0:
                res.append(cur.copy())
                return
            for i in range(pos,len(candidates)):
                if i>pos and candidates[i-1]==candidates[i]:
                    continue
                if candidates[i]>target:
                    break
                cur.append(candidates[i])
                backtrack(i+1,cur,target-candidates[i])
                cur.pop()
        backtrack(0,[],target)
        return res