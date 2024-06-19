class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        fre = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = 1+count.get(i,0)
        for n,c in count.items():
            fre[c].append(n)
        res = []
        for i in range(len(fre)-1,-1,-1):
            for j in fre[i]:
                res.append(j)
                if len(res)==k:
                    return res