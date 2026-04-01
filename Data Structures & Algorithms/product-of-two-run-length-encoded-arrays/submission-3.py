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
                r[0] = mult
            else:
                r = res[-1] # Extract prev val-freq pair if curr mult is equal 

            if r[1] == 0: # Means we have a new val-freq pair, so we need to append
                r[1] = min_freq
                res.append(r)
            else:
                r[1] += min_freq # Otherwise we just update the freq

            encoded1[en1][1] -= min_freq
            encoded2[en2][1] -= min_freq

            # We update pointers if freq is <= 0 | to get new val-freq pair
            if encoded1[en1][1] <= 0:
                en1 += 1
            if encoded2[en2][1] <= 0:
                en2 += 1


        return res
