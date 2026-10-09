class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, arr, left, right):
        if right - left + 1 <= 1:
            return arr

        pivot = arr[right]
        start = left

        for k in range(left, right):
            if arr[k] < pivot:
                temp = arr[start]
                arr[start] = arr[k]
                arr[k] = temp
                start += 1

        arr[right] = arr[start]
        arr[start] = pivot

        self.quick_sort(arr, left, start - 1)
        self.quick_sort(arr, start + 1, right)
