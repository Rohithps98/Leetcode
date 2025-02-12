# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        \\\Encodes a tree to a single string.
        \\\
        def preorder(node):
            if not node:
                return []
            return [str(node.val)]+preorder(node.left)+preorder(node.right)
        return ' '.join(preorder(root))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        \\\Decodes your encoded data to tree.
        \\\
        if not data:
            return None
        values = list(map(int,data.split()))
        index = 0
        def buildbst(minval,maxval):
            nonlocal index
            if index>=len(values) or values[index]>maxval or values[index]<minval:
                return None
            val = values[index]
            index+=1
            node = TreeNode(val)
            node.left = buildbst(minval,val)
            node.right = buildbst(val,maxval)
            return node
        return buildbst(float('-inf'),float('inf'))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans