class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'[':']','{':'}','(':')'}
        st = []
        for i in s:
            if i in pairs:
                st.append(i)
            elif len(st)==0 or i!=pairs[st.pop()]:
                return False
        return len(st)==0