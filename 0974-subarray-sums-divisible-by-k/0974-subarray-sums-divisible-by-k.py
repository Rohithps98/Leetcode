class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rc = {0:1}
        rs = 0
        count = 0
        for num in nums:
            rs+=num
            remainder = rs%k
            if remainder<0:
                remainder+=k
            if remainder in rc:
                count+=rc[remainder]
                rc[remainder]+=1
            else:
                rc[remainder] = 1
        return count