class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        baseline = int(n * (n+1) / 2)
        seen = set()
        total = 0

        dupe = None
        
        for num in nums:
            if num in seen:
                dupe = num
            seen.add(num)
            total += num

        return [dupe, (dupe + baseline - total)]
            