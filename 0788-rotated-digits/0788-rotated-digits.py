class Solution:
    def rotatedDigits(self, n: int) -> int:
        def is_good(nums,dp):
            if nums in dp:
                return dp[nums]
            rotated = {'0':'0','1':'1','2':'5','5':'2','6':'9','8':'8','9':'6'}
            rotated_num = ''
            for digit in str(nums):
                if digit in ['3','4','7']:
                    dp[digit] = False
                    return False
                else:
                    rotated_num+=rotated[digit]
            dp[nums] = rotated_num!=str(nums)
            return dp[nums]
        dp = {}
        count = 0
        for i in range(1,n+1):
            if is_good(i,dp):
                count+=1
        return count