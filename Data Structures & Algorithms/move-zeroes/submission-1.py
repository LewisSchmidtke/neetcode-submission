class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos_idx = deque()

        for idx, number in enumerate(nums):
            if number == 0:
                pos_idx.append(idx)
            else:
                if pos_idx:
                    new_pos = pos_idx.popleft()
                    nums[new_pos] = number
                    nums[idx] = 0
                    pos_idx.append(idx)
        