class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st = []
        pl = len(part)
        for c in s:
            st.append(c)
            if len(st)>=pl and ''.join(st[-pl:])==part:
                del st[-pl:]
        return ''.join(st)