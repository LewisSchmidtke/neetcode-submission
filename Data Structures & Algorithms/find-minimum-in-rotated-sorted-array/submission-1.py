class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + ((right - left) // 2)
            l_val, m_val, r_val = nums[left], nums[mid], nums[right]

            max_val = max(l_val, m_val, r_val)

            if max_val == r_val:
                right = mid
            elif max_val == l_val:
                left = mid
            else:
                if m_val > l_val:
                    left = mid 
                else: 
                    right = mid 

        
        return nums[left]

            