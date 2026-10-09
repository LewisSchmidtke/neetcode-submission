class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        unique = set()
        seen = set()

        for num in nums:
            if num in unique:
                seen.add(num)
                unique.remove(num)
            else:
                unique.add(num)

        l = sorted(list(unique))
        
        if l:
            return l[-1]
        else:
            return -1