class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.eow = True
    def dfs(self):
        stack = [(self.root,'')]
        longest = ''
        while stack:
            node,path = stack.pop()
            if node.eow:
                if len(path)>len(longest):
                    longest = path
                elif len(path)==len(longest) and path<longest:
                    longest = path
            for char,child in node.children.items():
                if child.eow:
                    stack.append((child,path+char))
        return longest
                
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.dfs()