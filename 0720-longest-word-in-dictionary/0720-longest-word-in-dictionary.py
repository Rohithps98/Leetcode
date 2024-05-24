class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        wordset = set([''])
        longest = ''
        for word in words:
            if word[:-1] in wordset:
                wordset.add(word)
                if len(word)>len(longest):
                    longest = word
        return longest