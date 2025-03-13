# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
            if not root:
                return []
            q = deque()
            q.append(root)
            output = []
            while q:
                ncl = []
                l = len(q)
                for _ in range(l):
                    curr = q.popleft()
                    ncl.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                output.append(ncl)
            return output[::-1]