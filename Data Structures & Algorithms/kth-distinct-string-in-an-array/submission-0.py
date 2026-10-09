class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        chars = {}
        removed = set()

        for index, c in enumerate(arr):
            if c in removed:
                continue

            if c in chars:
                del chars[c]
                removed.add(c)
                continue

            chars[c] = index

        uniques = sorted(list(chars.items()), key= lambda x: x[1])
        try:
            ret = uniques[k - 1][0]
            return ret
        except IndexError:
            return ""