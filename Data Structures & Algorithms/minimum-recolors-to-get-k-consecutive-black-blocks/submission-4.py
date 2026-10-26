class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minR = k
        wCount = 0
        l = 0

        for r in range(len(blocks)):
            if blocks[r] == "W":
                wCount += 1

            if r - l + 1 == k:
                minR = min(minR, wCount)
                if blocks[l] == "W":
                    wCount -= 1
                l += 1
        
        return minR