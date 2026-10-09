class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")  # Format: "length#string"
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#": # Find the delimiter to know where the length ends
                j += 1
            
            length = int(s[i:j])
            
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            i = end
            
        return res


    # def encode(self, strs: List[str]) -> str:
    #     res = []
    #     for word in strs:
    #         w = []
    #         for char in word:
    #             w.append(f"{ord(char)}")
    #             w.append("/")
    #         res.append("".join(w))
    #         res.append(",")
    #     return "".join(res)

    # def decode(self, s: str) -> List[str]:
    #     words = s.split(",")[:-1]
    #     res = []
    #     for word in words:
    #         dec_word = []
    #         chars = word.split("/")[:-1]
    #         for order in chars:
    #             dec_word.append(chr(int(order)))

    #         res.append("".join(dec_word))

    #     return res

