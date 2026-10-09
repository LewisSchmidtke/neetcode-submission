class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_table_s = {}
        hash_table_t = {}

        for index, char_s in enumerate(s):
            if char_s not in hash_table_s:
                hash_table_s[char_s] = 1
            else:
                hash_table_s[char_s] += 1
            
            if t[index] not in hash_table_t:
                hash_table_t[t[index]] = 1
            else:
                hash_table_t[t[index]] += 1

        if hash_table_s == hash_table_t:
            return True
        
        return False
