class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.checkPalindrome(word):
                return word
        
        return ""
    

    def checkPalindrome(self, w):
        left = 0
        right = len(w) - 1

        while left <= right:
            if w[left] != w[right]:
                return False
            left += 1
            right -= 1

        return True



