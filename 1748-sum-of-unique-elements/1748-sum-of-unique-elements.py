class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        c = 0
        for i,j in a.items():
            if j==1:
                c+=i
        return c