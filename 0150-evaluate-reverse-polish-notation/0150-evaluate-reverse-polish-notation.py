class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        def isop(s):
            return s in ['+','-','*','/']
        for i in tokens:
            if isop(i):
                b = int(st.pop())
                a = int(st.pop())
                if i=='+':
                    res = a+b
                if i =='-':
                    res = a-b
                if i=='*':
                    res = a*b
                if i=='/':
                    res = int(a/b)
                st.append(str(res))
            else:
                st.append(i)
        return int(st.pop())