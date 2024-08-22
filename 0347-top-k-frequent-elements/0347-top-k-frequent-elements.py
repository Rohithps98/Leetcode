class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # freq = [[] for i in range(len(nums)+1)]
        # for i in nums:
        #     count[i] = 1+count.get(i,0)
        # for n,c in count.items():
        #     freq[c].append(n)
        # res = []
        # for i in range(len(freq)-1,-1,-1):
        #     for j in freq[i]:
        #         res.append(j)
        #         if len(res)==k:
        #             return res
        count = {}
        for i in nums:
            count[i] = 1+count.get(i,0)
        a = []
        for i,j in count.items():
            a.append((i,j))
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[i][1]<a[j][1]:
                    a[i],a[j] = a[j],a[i]
        res = []
        for i in range(k):
            res.append(a[i][0])
        return res