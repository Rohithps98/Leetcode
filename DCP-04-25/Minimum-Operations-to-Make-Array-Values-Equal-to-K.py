class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # a = list(set(nums))
        # if len(a) == 1 and a[0] == k:
        #     return 0
        # count = 0
        # for i in a:
        #     if i > k:
        #         count += 1
        #     if i < k:
        #         return -1
        # return count if count > 0 else -1
        st = set()
        for x in nums:
            if x < k:
                return -1
            elif x > k:
                st.add(x)
        return len(st)