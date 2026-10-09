class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Simple solution count values in hashmap if counted value is > n/2 return corresponding key O(n) time and space

        # Second solution -> sort nums and return value at n // 2

        # Third solution: Boyer Moore Voting

        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            
            if res == num:
                count += 1
            else:
                count -= 1

        return res

