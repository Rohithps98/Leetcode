# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        st = [(root,\\)]
        while st:
            node,path = st.pop()
            if node:
                path+=str(node.val)
                if not(node.left or node.right):
                    res+=int(path,2)
                else:
                    st.append((node.left,path))
                    st.append((node.right,path))
        return res