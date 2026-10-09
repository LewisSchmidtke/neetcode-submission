class Solution:
    def validPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        swaps = 0

        while front <= back:

            if s[front] == s[back]:
                front += 1
                back -= 1
                continue

            swaps += 1
            if swaps > 1:
                return False

            if s[front + 1] == s[back]:
                front += 2
                back -= 1

            elif s[front] == s[back - 1]:
                front += 1
                back -= 2
            
            else:
                return False

        return True

