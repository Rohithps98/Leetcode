class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        while l<r:
            su = numbers[l]+numbers[r]
            if su==target:
                return [l+1,r+1]
            if su<target:
                l+=1
            elif su>target:
                r-=1
            