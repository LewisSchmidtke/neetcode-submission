class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ref = sorted(heights)
        counter = 0

        for index, h in enumerate(heights):
            if h != ref[index]:
                counter += 1

        return counter