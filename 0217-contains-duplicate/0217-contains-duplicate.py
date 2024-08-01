class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for i in nums:
            a[i] = 1+a.get(i,0)
            if a[i]>1:
                return True
        return False
        # a = set()
        # for i in nums:
        #     if i in a:
        #         return True
        #     a.add(i)
        # return False