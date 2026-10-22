class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        idx_heights = sorted([(height, idx) for idx, height in enumerate(heights)], reverse=True)
        res = []
        for _, i in idx_heights:
            res.append(names[i])
        
        return res
