class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9+7
        oddcount = 0
        evencount = 1
        prefixsum = 0
        oddsubarray = 0
        for i in arr:
            prefixsum+=i
            if prefixsum%2==1:
                oddsubarray+=evencount
                oddcount+=1
            else:
                oddsubarray+=oddcount
                evencount+=1
        oddsubarray%=mod
        return oddsubarray