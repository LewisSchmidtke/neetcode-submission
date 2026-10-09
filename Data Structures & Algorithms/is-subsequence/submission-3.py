class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if len_s > len_t: 
            return False

        valid = 0
        t_pointer = 0
        for c in s:
            while t_pointer < len_t:
                if c == t[t_pointer]:
                    t_pointer += 1
                    valid += 1
                    break
                
                t_pointer += 1
            
            if t_pointer >= len_t and valid != len_s:
                return False
        
        return valid == len_s


            


