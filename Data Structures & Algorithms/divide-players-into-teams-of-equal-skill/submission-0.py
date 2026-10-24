class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        baseline = None
        chem = 0

        left = 0
        right = len(skill) - 1

        while left < right:
            s = skill[left] + skill[right]
            if baseline is None:
                baseline = s
            else:
                if s != baseline:
                    return -1

            chem += (skill[left] * skill[right])
            left += 1
            right -= 1
        
        return chem
            
