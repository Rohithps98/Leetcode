# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ma = 0
        st = [(root,1)]
        while st:
            node,d = st.pop()
            if node.left:
                st.append((node.left,d+1))
            if node.right:
                st.append((node.right,d+1))
            ma = max(ma,d)
        return ma