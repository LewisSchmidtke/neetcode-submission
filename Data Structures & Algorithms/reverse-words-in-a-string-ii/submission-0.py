class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Reverse whole array
        left = 0
        right = len(s) - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        # Reverse each word
        left = right = len(s) - 1
        while left >= 0:
            
            while left - 1 >= 0 and s[left - 1] != " ":
                left -= 1
            
            temp = left
            while left <= right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            left = temp - 1
            right = temp - 2