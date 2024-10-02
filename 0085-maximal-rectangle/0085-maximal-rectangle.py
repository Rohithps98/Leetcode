# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         if not matrix:
#             return 0
#         def largestrectanglearea(heights):
#             max_area = 0
#             st = []
#             heights.append(0)
#             for i in range(len(heights)):
#                 while st and heights[i]<heights[st[-1]]:
#                     h = heights[st.pop()]
#                     w = i if not st else i-st[-1]-1
#                     max_area = max(max_area,h*w)
#                 st.append(i)
#             heights.pop()
#             return max_area
#         max_area = 0
#         n = len(matrix[0])
#         heights = [0]*n
#         for row in A:
#             for i in range(n):
#                 heights[i] = heights[i]+1 if row[i]==1 else 0
#             max_area = max(max_area,largestrectanglearea(heights))
#         return max_area
class Solution:
    def maximalRectangle(self, A):
        if not A:
            return 0
        def largestrectanglearea(heights):
            max_area = 0
            st = []
            heights.append(0)
            for i in range(len(heights)):
                while st and heights[i]<heights[st[-1]]:
                    h = heights[st.pop()]
                    w = i if not st else i-st[-1]-1
                    max_area = max(max_area,h*w)
                st.append(i)
            heights.pop()
            return max_area
        max_area = 0
        n = len(A[0])
        heights = [0]*n
        for row in A:
            for i in range(n):
                heights[i] = heights[i]+1 if row[i]=="1" else 0
            max_area = max(max_area,largestrectanglearea(heights))
        return max_area