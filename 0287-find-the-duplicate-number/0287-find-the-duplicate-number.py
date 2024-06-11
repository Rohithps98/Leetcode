class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast,slow1 = 0,0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        while True:
            slow = nums[slow]
            slow1 = nums[slow1]
            if slow==slow1:
                break
        return slow