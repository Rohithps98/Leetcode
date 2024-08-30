class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        st = []
        for i,t in enumerate(temperatures):
            while st and st[-1][1]<t:
                sti,stt = st.pop()
                res[sti] = i-sti
            st.append([i,t])
        return res