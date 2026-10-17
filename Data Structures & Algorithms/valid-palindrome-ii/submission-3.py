class Solution:
    def validPalindrome(self, s: str) -> bool:
        preprocessedString = self.preprocess_string(s)

        charChanges = 0

        left = 0
        right = len(preprocessedString) - 1

        while left <= right:
            while left <= right and not preprocessedString[left].isalnum():
                left += 1
            while right <= left and not preprocessedString[right].isalnum():
                right -= 1
            
            if left > right:
                break
            
            if preprocessedString[left] != preprocessedString[right]:
                valid = self.check_palindrome(left + 1, right, s) or self.check_palindrome(left, right - 1, s)
                return valid

            left += 1
            right -= 1



        return charChanges <= 1
        

    def preprocess_string(self, string: str) -> str:
        string = string.lower()
        string = string.strip()

        return string

    def check_palindrome(self, l: int, r: int, string: str) -> bool:
        while l <= r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        
        return True











