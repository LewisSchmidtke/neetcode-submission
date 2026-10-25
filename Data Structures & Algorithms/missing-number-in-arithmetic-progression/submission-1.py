class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        interval = arr[-1] - arr[0]
        jumps = int(interval/len(arr))

        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] == arr[0] + mid * jumps:
                left = mid + 1
            else:
                right = mid
        
        return arr[0] + left * jumps