class Solution:
    def trap(self, height: List[int]) -> int:
        res,l,r = 0,0,len(height)-1
        lm,rm = height[l],height[r]
        while l<r:
            if lm<rm:
                l+=1
                lm = max(height[l],lm)
                dl = lm-height[l]
                if dl>0:
                    res+=dl
            else:
                r-=1
                rm = max(height[r],rm)
                dr = rm-height[r]
                if dr>0:
                    res+=dr
        return res