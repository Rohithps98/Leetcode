class Solution:
    def smallestNumber(self, pattern: str) -> str:
        st = []
        res = []
        for i in range(len(pattern)+1):
            st.append(str(i+1))
            if i==len(pattern) or pattern[i] == 'I':
                while st:
                    res.append(st.pop())
        return ''.join(res)