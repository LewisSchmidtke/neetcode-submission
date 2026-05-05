class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)

        count = 0
        num = arr[0]
        for n in arr:
            if n == num:
                count += 1
            else:
                if count == num:
                    return num
                num = n
                count = 1

        if num == count:
            return num
        
        return -1
                
