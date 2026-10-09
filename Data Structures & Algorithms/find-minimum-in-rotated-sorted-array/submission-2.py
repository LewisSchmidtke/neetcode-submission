class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            l_val, m_val, r_val = nums[left], nums[mid], nums[right]

            if l_val < r_val:
                return min(result, l_val)

            result = min(result, m_val)

            if m_val >= l_val:
                left = mid + 1
            else:
                right = mid - 1

        
        return result

            