class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cache = [[-1] * 2 for _ in range(len(nums))]

        def traverse(index, flag):
            if index >= len(nums) or (flag and index == len(nums) - 1): # Out of bounds or first house was robbed and index = last house
                return 0 

            if cache[index][flag] != -1:
                return cache[index][flag]

            cache[index][flag] = max(
                traverse(index + 1, flag), # Skip current
                nums[index] + traverse(index + 2, flag) # Steal and skip next
                )

            return cache[index][flag]
        
        return max(traverse(0, True) , traverse(1, False))