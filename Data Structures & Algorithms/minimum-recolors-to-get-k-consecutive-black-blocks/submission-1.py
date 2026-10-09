class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ops = 0
        for j in range(k): # k not inclusive 
            if blocks[j] == "W":
                ops += 1
        
        res = ops
        
        for i in range(k, len(blocks)): # starting from k
            if blocks[i - k] == "W":
                ops -= 1
            if blocks[i] == "W":
                ops += 1
            res = min(res, ops)

        return res

            

