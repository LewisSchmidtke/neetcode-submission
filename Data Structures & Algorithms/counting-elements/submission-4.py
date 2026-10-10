class Solution:
    def countElements(self, arr: List[int]) -> int:
        values = set(arr)

        count = 0
        for number in arr:
            if (number + 1) in values:
                count += 1

        return count