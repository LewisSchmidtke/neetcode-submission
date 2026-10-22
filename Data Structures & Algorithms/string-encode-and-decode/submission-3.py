class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for string in strs:
            enc = enc + f"{len(string)}#{string}"
        
        return enc

    def decode(self, s: str) -> List[str]:
        left = right = 0
        res = []

        while right < len(s):
            word_length = ""
            while s[right] != "#":
                word_length = word_length + f"{s[right]}"
                right += 1
            right += 1
            length = int(word_length)
            left = right
            right = right + length
            
            res.append(s[left: right])

        return res

