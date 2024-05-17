class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_radius = 0
        for house in houses:
            leftheater = self.findclosestheater(heaters,house)
            rightheater = leftheater+1
            if leftheater>=0:
                distanceleft = abs(house-heaters[leftheater])
            else:
                distanceleft = float(inf)
            if rightheater<len(heaters):
                distanceright = abs(house-heaters[rightheater])
            else:
                distanceright = float(inf)
            max_radius = max(max_radius,min(distanceleft,distanceright))
        return max_radius
    def findclosestheater(self,heaters,target):
        left,right = 0,len(heaters)-1
        while left<=right:
            mid = (left+right)//2
            if heaters[mid]==target:
                return mid
            elif heaters[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return right