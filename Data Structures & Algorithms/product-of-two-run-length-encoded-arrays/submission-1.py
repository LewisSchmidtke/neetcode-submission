class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        decoded1 = []

        for seq in encoded1:
            dec = [seq[0]] * seq[1]
            decoded1.extend(dec)

        left = 0
        enc2 = 0
        print(decoded1)
        while left < len(decoded1) and enc2 < len(encoded2):
            counter = encoded2[enc2][1]
            while counter > 0:
                decoded1[left] *= encoded2[enc2][0]
                left += 1
                counter -= 1
            enc2 += 1

        res = []

        left = right = 0
        while right < len(decoded1):
            number = decoded1[left]
            while right < len(decoded1) and decoded1[right] == number:
                right += 1
            
            res.append([number, right - left])
            left = right
            right += 1

        return res


        


