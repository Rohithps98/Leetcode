class Solution:
    def rotatedDigits(self, n: int) -> int:
        def is_good(nums):
            rotated = {'1':'1','2':'5','5':'2','6':'9','8':'8','9':'6','0':'0'}
            rotated_num = ""
            for digit in str(nums):
                if digit in ['3','4','7']:
                    return False
                else:
                    rotated_num+=rotated[digit]
            return rotated_num!=str(nums)
        count= 0
        for i in range(1,n+1):
            if is_good(i):
                count+=1
        return count