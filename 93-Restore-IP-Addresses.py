class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(start,path):
            if len(path)==4:
                if start == len(s):
                    res.append('.'.join(path))
                return
            for end in range(start,min(start+3,len(s))):
                segment = s[start:end+1]
                if (segment[0]=='0' and len(segment)>1) or int(segment)>255:
                    continue
                backtrack(end+1,path+[segment])
        backtrack(0,[])
        return res