class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_point = 0
        t_point = 0

        while s_point < len(s) and t_point < len(t):
            if s[s_point] == t[t_point]:
                s_point += 1
                t_point += 1
            else:
                s_point += 1
        
        return len(t) - t_point