class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ma = 0
        st = []
        for i,h in enumerate(heights):
            start = i
            while st and st[-1][1]>h:
                index,height = st.pop()
                ma = max(ma,height*(i-index))
                start = index
            st.append([start,h])
        for i,h in st:
            ma = max(ma,h*(len(heights)-i))
        return ma