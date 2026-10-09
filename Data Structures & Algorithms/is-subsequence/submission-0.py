class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_point = len(s) - 1
        t_point = len(t) - 1

        while t_point >= 0 and s_point >= 0:
            if s[s_point] == t[t_point]:
                s_point -= 1
                t_point -= 1
            else:
                t_point -= 1
        
        if s_point < 0:
            return True
        else:
            return False