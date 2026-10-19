class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left = 0
        right = k - 1

        tupled = [(x, i) for i, x in enumerate(nums[left:right+1])]
        heapq.heapify_max(tupled)

        res = []

        while right < len(nums):
            while tupled and tupled[0][1] < left: # Remove elements outside the current window
                heapq.heappop_max(tupled)

            max_val, max_index = tupled[0] # Peek at max (don't pop)
            res.append(max_val)

            right += 1
            left += 1

            if right < len(nums):
                heapq.heappush_max(tupled, (nums[right], right))

        return res
