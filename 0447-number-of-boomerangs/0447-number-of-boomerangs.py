class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boom = 0
        for p1 in points:
            distance = defaultdict(int)
            for p2 in points:
                if p1==p2:
                    continue
                dist = (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
                distance[dist]+=1
            for dist in distance.values():
                boom+=dist*(dist-1)
        return boom