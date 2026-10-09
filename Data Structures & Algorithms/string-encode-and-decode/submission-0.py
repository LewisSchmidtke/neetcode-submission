class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            w = ""
            for char in word:
                w += f"{ord(char)}"
                w += "/"
            res += w
            res += ","
        return res

    def decode(self, s: str) -> List[str]:
        words = s.split(",")[:-1]
        res = []
        for word in words:
            dec_word = ""
            chars = word.split("/")[:-1]
            for order in chars:
                dec_word += chr(int(order))

            res.append(dec_word)

        return res

