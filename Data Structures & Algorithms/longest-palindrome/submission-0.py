class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = [0] * 52

        for c in s:
            freq[ord(c) - ord("a")] += 1
        
        unevens = 0
        length = 0
        print(freq)
        for count in freq:
            if count == 0:
                continue
            if count % 2 != 0:
                unevens += 1
            

            length += (2 * (count // 2))
        
        
        if unevens >= 1:
            length += 1
        
        return length
            