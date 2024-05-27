# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.issame(root.left,root.right)
    def issame(self,left,right):
        if left==None and right==None:
            return True
        if left==None or right==None:
            return False
        if left.val!=right.val:
            return False
        return self.issame(left.right,right.left) and self.issame(left.left,right.right)