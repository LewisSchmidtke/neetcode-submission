class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []

        en1 = 0
        en2 = 0

        while en1 < len(encoded1) and en2 < len(encoded2):
            mult = int(encoded1[en1][0] * encoded2[en2][0])
            freq1 = encoded1[en1][1]
            freq2 = encoded2[en2][1]
            min_freq = min(freq1, freq2)

            if len(res) == 0 or len(res) >= 1 and res[-1][0] != mult:
                r = [0,0] # Reset and create new rle value freq pair
            else:
                r = res[-1]

            r[0] = mult
            
            if r[1] == 0:
                r[1] = min_freq
                res.append(r)

            else:
                r[1] += min_freq


            # Update freq or pointer
            if freq1 - min_freq <= 0:
                en1 += 1
            else:
                encoded1[en1][1] -= min_freq

            if freq2 - min_freq <= 0:
                en2 += 1
            else:
                encoded2[en2][1] -= min_freq

        return res

            

            




