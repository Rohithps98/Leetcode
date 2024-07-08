class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = {}
        b = []
        for i in nums:
            a[i]=1+a.get(i,0)
        for i,count in a.items():
            if count>1:
                b.append(i)
        return b