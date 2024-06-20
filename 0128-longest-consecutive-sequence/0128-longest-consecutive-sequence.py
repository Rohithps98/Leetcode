class Solution:
    def find(self,par,res):
        if par[res]!=res:
            par[res] = self.find(par,par[res])
        return par[res]
    def union(self,par,rank,size,x,y):
        res1 = self.find(par,x)
        res2 = self.find(par,y)
        if res1!=res2:
            if rank[res1]>rank[res2]:
                par[res2] = res1
                size[res1]+=size[res2]
            elif rank[res2]<rank[res1]:
                par[res1]=res2
                size[res2]+=size[res1]
            else:
                par[res2] = res1
                rank[res1]+=1
                size[res1]+=size[res2]
    def longestConsecutive(self, nums: List[int]) -> int:
        par,rank,size={},{},{}
        for i in nums:
            par[i]=i
            rank[i]=0
            size[i]=1
        for i in nums:
            if i+1 in par:
                self.union(par,rank,size,i,i+1)
        ms = 0
        for i in nums:
            ms = max(ms,size[self.find(par,i)])
        return ms
        # n = set(nums)
        # lo = 0
        # for i in nums:
        #     if i-1 not in n:
        #         l = 0
        #         while i+l in n:
        #             l+=1
        #         lo = max(lo,l)
        # return lo