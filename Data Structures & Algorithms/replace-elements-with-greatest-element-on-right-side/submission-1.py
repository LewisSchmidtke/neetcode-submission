class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = arr[-1]
        right_pointer = len(arr) - 1

        while right_pointer >= 0:
            if right_pointer < len(arr) - 1:
                temp = arr[right_pointer]
                arr[right_pointer] = current_max
                current_max = max(current_max, temp)
            else:
                arr[right_pointer] = -1

            right_pointer -= 1

        return arr
