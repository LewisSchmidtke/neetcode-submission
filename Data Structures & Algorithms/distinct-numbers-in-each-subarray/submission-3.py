class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums[:k]:
            counts[n] += 1
    
        res = [len(counts)]
        right = k
        left = 0

        while right < len(nums):
            removal = nums[left]
            counts[removal] -= 1

            if counts[removal] == 0:
                counts.pop(removal)

            left += 1

            adder = nums[right]
            counts[adder] += 1

            res.append(len(counts))
            right += 1

        return res


        



        