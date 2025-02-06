# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque, defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def bg(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            bg(node.left,node)
            bg(node.right,node)
        bg(root,None)
        visit = set()
        visit.add(target.val)
        q = deque([(target.val,0)])
        while q:
            if q[0][1]==k:
                return [node for node,_ in q]
            for _ in range(len(q)):
                node,dist = q.popleft()
                for nei in graph[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei,dist+1))
        return []