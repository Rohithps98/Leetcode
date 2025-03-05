class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findpivot(arr):
            l,r = 0,len(arr)-1
            while l<r:
                mid = (l+r)//2
                if arr[mid]>arr[r]:
                    l = mid+1
                else:
                    r = mid
            return l
        def binarysearch(arr,target,l,r):
            while l<=r:
                mid = (l+r)//2
                if arr[mid]==target:
                    return mid
                elif arr[mid]>target:
                    r = mid-1
                else:
                    l = mid+1
            return -1
        pivot = findpivot(nums)
        if nums[pivot]<=target<=nums[-1]:
            return binarysearch(nums,target,pivot,len(nums)-1)
        else:
            return binarysearch(nums,target,0,pivot-1)