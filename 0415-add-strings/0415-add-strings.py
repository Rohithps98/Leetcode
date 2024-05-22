class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j,carry,result = len(num1)-1,len(num2)-1,0,[]
        def chrtoint(ch):
            return ord(ch)-ord('0')
        while i>=0 or j>=0 or carry:
            n1 = chrtoint(num1[i]) if i>=0 else 0
            n2 = chrtoint(num2[j]) if j>=0 else 0
            total = n1+n2+carry
            carry = total//10
            result.append(chr(total%10+ord('0')))
            i-=1
            j-=1
        return ''.join(result[::-1])