class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        cs = ''
        cn = 0
        for i in s:
            if i.isdigit():
                cn = cn*10+int(i)
            elif i=='[':
                st.append(cn)
                st.append(cs)
                cs = ''
                cn = 0
            elif i==']':
                ps = st.pop()
                pn = st.pop()
                cs = ps+cs*pn
            else:
                cs+=i
        while st:
            cs+=st.pop()
        return cs