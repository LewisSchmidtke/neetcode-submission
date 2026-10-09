class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        right_max = -1
        right = len(arr) - 1
        while right >= 0:
            temp = arr[right]
            arr[right] = right_max
            if temp > right_max:
                right_max = temp
                
            right -= 1

        return arr

