class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}

        for string in strs:
            temp = string
            character_sort = "".join(sorted(string))
            
            if character_sort in word_map:
                word_map[character_sort].append(temp)
            else:
                word_map[character_sort] = [temp]
        
        res = []
        for groups in word_map.values():
            res.append(groups)
        
        return res
