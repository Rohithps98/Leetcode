from collections import defaultdict
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        countmap = defaultdict(int)
        for num in nums2:
            countmap[num*k]+=1
        c = 0
        for i in nums1:
            for d in countmap:
                if i%d==0:
                    c+=countmap[d]
        return c
        # a = 0
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i]%(nums2[j]*k)==0:
        #             a+=1
        # return a