class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # v1 = version1.split(\.\)
        # v2 = version2.split(\.\)
        # if len(v1)>len(v2):
        #     v2 = v2+[0]*(len(v1)-len(v2))
        # else:
        #     v1 = v1+[0]*(len(v2)-len(v1))
        # for i in range(len(v1)):
        #     if int(v1[i])>int(v2[i]):
        #         return 1
        #     elif int(v1[i])==int(v2[i]):
        #         continue
        #     else:
        #         return -1
        # return 0
        for v1,v2 in zip_longest(version1.split(\.\),version2.split(\.\), fillvalue = '0'):
            if int(v1)>int(v2):
                return 1
            elif int(v2)>int(v1):
                return -1
        return 0
