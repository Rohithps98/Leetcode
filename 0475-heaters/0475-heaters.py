class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        maxradius = 0
        for house in houses:
            leftheater = self.nearestheater(heaters,house)
            rightheater = leftheater+1
            if leftheater>=0:
                distanceleft = abs(house-heaters[leftheater])
            else:
                distanceleft = float('inf')
            if rightheater<len(heaters):
                distanceright= abs(house-heaters[rightheater])
            else:
                distanceright= float('inf')
            maxradius = max(maxradius,min(distanceleft,distanceright))
        return maxradius
    def nearestheater(self,heaters,house):
        left,right = 0,len(heaters)-1
        while left<=right:
            mid = (left+right)//2
            if heaters[mid]==house:
                return mid
            elif heaters[mid]<house:
                left = mid+1
            else:
                right = mid-1
        return right