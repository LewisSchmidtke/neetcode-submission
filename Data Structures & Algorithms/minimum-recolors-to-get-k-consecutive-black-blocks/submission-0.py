class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = 1

        ops = 1 if blocks[left] == "W" else 0
        while right < k:
            if blocks[right] == "W":
                ops += 1
            right += 1
        
        min_ops = ops
        left = 1
        right += 1
        while right < len(blocks):
            if blocks[right] == "W":
                ops += 1
            if blocks[left] == "W":
                ops -= 1
            min_ops = min(min_ops, ops)
            right += 1
            left += 1

        return min_ops


            

