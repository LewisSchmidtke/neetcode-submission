class Solution:
    def trap(self, height: List[int]) -> int:
        def find_water_in_area(left_h: int, left_pos: int, right_h: int, right_pos: int, trapped_blocks: int) -> int:
            """
            Calculates the trapped water in a distinct sub area
            Args:
                left_h (int): height of left bounding pillar
                left_pos (int): x-position of left bounding pillar
                right_h (int): height of right bounding pillar
                right_pos (int): x-position of right bounding pillar
                trapped_blocks (int): nr of blocks in between left and right pillar
            Returns:
                int: The amount of trapped rainwater in specified boundary
            """
            # First find maximum shared height
            shared_height = min(left_h, right_h)
            width_in_between = right_pos - left_pos - 1
            theoretical_max_trapped = width_in_between * shared_height
            actual_trapped = max(0, theoretical_max_trapped - trapped_blocks) # Account for theoretical being 0
            return actual_trapped


        left_pointer = 0
        left_height = height[left_pointer]
        blocks_inbetween = 0
        total_trapped = 0
        
        for right in range(1, len(height)):
            if height[right] >= left_height:
                current_trapped = find_water_in_area(left_height, left_pointer, height[right], right, blocks_inbetween)
                total_trapped += current_trapped
                blocks_inbetweem = 0
                left_pointer = right
                left_height = height[right]
            else:
                blocks_inbetween += height[right]

        return total_trapped
            

