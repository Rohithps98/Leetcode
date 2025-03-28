# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder.pop())
        inorderindex = inorder.index(root.val)
        root.right = self.buildTree(inorder[inorderindex+1:],postorder)
        root.left = self.buildTree(inorder[:inorderindex],postorder)
        return root