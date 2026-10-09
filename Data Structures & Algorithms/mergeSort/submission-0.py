# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.merge_sort_help(pairs, 0, len(pairs) - 1)

    def merge_sort_help(self, arr, start, end):
        if end - start + 1 <= 1:
            return arr

        middle = (start + end) // 2

        self.merge_sort_help(arr, start, middle)
        self.merge_sort_help(arr, middle + 1, end)

        self.merge(arr, start, middle, end)

        return arr

    def merge(self, arr, start, middle, end):
        left_arr = arr[start : middle + 1]
        right_arr = arr[middle + 1 : end + 1]

        left = 0
        right = 0
        merge_p = start

        while left < len(left_arr) and right < len(right_arr):
            if left_arr[left].key <= right_arr[right].key:
                arr[merge_p] = left_arr[left]
                left += 1
            else:
                arr[merge_p] = right_arr[right]
                right += 1

            merge_p += 1

        while left < len(left_arr):
            arr[merge_p] = left_arr[left]
            left += 1
            merge_p += 1

        while right < len(right_arr):
            arr[merge_p] = right_arr[right]
            right += 1
            merge_p += 1
            



