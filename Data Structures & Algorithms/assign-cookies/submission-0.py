class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        children = sorted(g)
        cookies = sorted(s)

        ch = len(children) - 1
        co = len(cookies) - 1

        fulfilled = 0
        while ch >= 0 and co >= 0:
            if cookies[co] >= children[ch]:
                fulfilled += 1
                co -= 1

            ch -= 1
            

        return fulfilled


