class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # len(heights) always greater 2
        # heights[i] >= 0

        # we initialize the two pointers left and right
        left = 0
        right = len(heights) - 1

        max_water_amount = 0

        # we calculate the current volume based on the container width (distance between the two) 
        # and the maximum shared height so min(heights[left], heights[right])
        while left < right:
            width = right - left
            shared_height = min(heights[left], heights[right])

            curr_water_amount = shared_height * width
            max_water_amount = max(max_water_amount, curr_water_amount)

            if heights[left + 1] > heights[right - 1]:
                left += 1
            else:
                right -= 1

        return max_water_amount