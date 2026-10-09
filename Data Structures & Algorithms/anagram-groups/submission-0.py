class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            freq = [0] * 26
            for c in string:
                freq[ord(c) - ord("a")] += 1

            freq = tuple(freq)

            if freq in res:
                res[freq].append(string)
            else:
                res[freq] = [string]

        return list(res.values())