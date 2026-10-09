class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        distance = 0
        l = 0
        r = 1
        uniques = 0

        while r < len(nums):
            if nums[l] != nums[r]: 
                uniques += 1
                if distance == 0:
                    l += 1
                    r += 1
                else:
                    l += 1
                    nums[l] = nums[r]
                    distance = 0
            else:
                r += 1
                distance += 1

        if len(nums) > 0:
            uniques += 1

        return uniques
                
