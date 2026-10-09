class Solution:
    def isArmstrong(self, n: int) -> bool:
        res = 0
        comp = n
        point = 8
        while point >= 0:
            magnitude = 1*10**point
            digit = comp // magnitude
            comp -= digit * magnitude

            if digit > 0:     
                res += digit ** 3
                
            point -= 1

        return res == n