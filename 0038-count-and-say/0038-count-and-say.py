class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        x = self.countAndSay(n-1)
        y = x[0]
        count = 1
        s = ""
        for i in range(1,len(x)):
            if x[i]==y:
                count+=1
            else:
                s+=str(count)
                s+=str(y)
                count = 1
                y = x[i]
        s+=str(count)
        s+=str(y)
        return s