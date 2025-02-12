class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(\ \,\\)
        st = []
        num = 0
        prevop = '+'
        for i,char in enumerate(s):
            if char.isdigit():
                num = num*10+int(char)
            if char in '+-*/' or i==len(s)-1:
                if prevop == '+':
                    st.append(num)
                elif prevop =='-':
                    st.append(-num)
                elif prevop == '/':
                    st.append(int(st.pop()/num))
                elif prevop == '*':
                    st.append(st.pop()*num)
                prevop = char
                num = 0
        return sum(st)