class Node:
    def __init__(self,val):
        self.val = val
        self.parent = self
        self.size = 1
class UnionFind:
    def find(self,node):
        if node!=node.parent:
            node.parent = self.find(node.parent)
        return node.parent
    def union(self,node1,node2):
        p1 = self.find(node1)
        p2 = self.find(node2)
        if p1!=p2:
            p2.parent = p1
            p1.size+=p2.size
        return p1.size
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind()
        nodes = {}
        ms = 0
        for num in nums:
            if num not in nodes:
                node = Node(num)
                nodes[num] = node
                size = 1
                if num+1 in nodes:
                    size = uf.union(node,nodes[num+1])
                if num-1 in nodes:
                    size = uf.union(node,nodes[num-1])
                ms = max(size,ms)
        return ms