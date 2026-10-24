class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        sPoint = 0
        gPoint = 0

        count = 0

        while sPoint < len(s) and gPoint < len(g): 

            if s[sPoint] >= g[gPoint]:
                count += 1
            else:
                sPoint += 1
                continue
            gPoint += 1
            sPoint += 1


        return count
