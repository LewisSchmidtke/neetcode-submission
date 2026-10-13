class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            shared_height = min(heights[left], heights[right])
            container_width = right - left 
            res = max(res, self.calculate_area(container_width, shared_height))

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return res


    def calculate_area(self, width, height):
        return width * height