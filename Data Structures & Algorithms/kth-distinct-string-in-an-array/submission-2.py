class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        unique = set()
        dupes = set()

        for string in arr:
            if string not in unique and string not in dupes:
                unique.add(string)
                continue
            if string in unique:
                unique.remove(string)
                dupes.add(string)
        count = 0
        for string in arr:
            if string in unique:
                count += 1
                if count == k:
                    return string
            
        return ""
            
