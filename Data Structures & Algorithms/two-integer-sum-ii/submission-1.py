class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Operation has to be ADDITION -> all numbers greater or equal to the target are irrelevant
        # List is sorted with increasing elements
        # Return 1-indexed solution -> add 1 to both indices -> [i1, i2] i1 < i2
        # O(1) Space

        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1] # One indexed
            elif current_sum < target:
                left += 1
            else: # cs larger than target
                right -= 1
