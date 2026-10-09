class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def first_occ_bs(target, up):
            l, r = 0, up
            while l < r:
                m = int((l + r) // 2)
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l

        start = first_occ_bs(target, n)
        if start == n or nums[start] != target:
            return [-1, -1]
        
        return [start, first_occ_bs(target + 1, n) - 1]

                