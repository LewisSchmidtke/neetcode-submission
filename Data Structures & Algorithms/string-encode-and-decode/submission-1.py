class Solution:
    # def encode(self, strs: List[str]) -> str:
    #     res = []
    #     for s in strs:
    #         # Format: "length#string"
    #         res.append(f"{len(s)}#{s}")
    #     return "".join(res)

    # def decode(self, s: str) -> List[str]:
    #     res = []
    #     i = 0
        
    #     while i < len(s):
    #         # Find the delimiter to know where the length ends
    #         j = i
    #         while s[j] != "#":
    #             j += 1
            
    #         # Get the length of the next string
    #         length = int(s[i:j])
            
    #         # Extract the string based on that length
    #         start = j + 1
    #         end = start + length
    #         res.append(s[start:end])
            
    #         # Move the pointer to the start of the next encoded block
    #         i = end
            
    #     return res


    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            w = []
            for char in word:
                w.append(f"{ord(char)}")
                w.append("/")
            res.append("".join(w))
            res.append(",")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        words = s.split(",")[:-1]
        res = []
        for word in words:
            dec_word = []
            chars = word.split("/")[:-1]
            for order in chars:
                dec_word.append(chr(int(order)))

            res.append("".join(dec_word))

        return res

