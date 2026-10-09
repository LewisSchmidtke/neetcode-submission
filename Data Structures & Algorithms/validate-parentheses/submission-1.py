class Solution:
    def isValid(self, s: str) -> bool:
        # Stack operation append(x), pop(-1)
        if len(s) == 1:
            return False
        
        mapping_dict = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }

        parenthesis_stack = []

        for p_char in s:
            if p_char not in mapping_dict:
                parenthesis_stack.append(p_char)
            else:
                try:
                    if parenthesis_stack[-1] == mapping_dict[p_char]:
                        parenthesis_stack.pop(-1)
                        continue
                    else:
                        return False
                except IndexError:
                    return False

        if parenthesis_stack:
            return False
        
        return True
    