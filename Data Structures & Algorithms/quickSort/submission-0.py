# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qs(pairs, 0, len(pairs) - 1)

        return pairs

    def qs(self, arr, start, end):
        if end - start + 1 <= 1:
            return arr # Base case

        pivot = arr[end]
        left = start

        for k in range(start, end):
            if arr[k].key < pivot.key:
                temp = arr[left]
                arr[left] = arr[k]
                arr[k] = temp
                left += 1
        # Swap partition val with val at left pointer
        arr[end] = arr[left]
        arr[left] = pivot

        self.qs(arr, start, left - 1)
        self.qs(arr, left + 1, end)
    


        