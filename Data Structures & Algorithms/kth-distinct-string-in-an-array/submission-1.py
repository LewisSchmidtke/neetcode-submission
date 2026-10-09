class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        unique = set()
        dupe = set()

        for index, c in enumerate(arr):
            if c in unique:
                unique.remove(c)
                dupe.add(c)

            if c not in dupe and c not in unique:
                unique.add(c)

        for c in arr:
            if c in unique:
                k -= 1
                if k == 0:
                    return c
        
        return ""

        