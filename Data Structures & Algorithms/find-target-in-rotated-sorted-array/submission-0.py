class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            m_val = nums[mid]

            if target == m_val:
                return mid

            elif target > m_val:
                left = mid + 1
            elif target < m_val:
                if target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1


