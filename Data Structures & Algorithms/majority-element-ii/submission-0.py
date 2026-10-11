class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3 + 1

        count_map = defaultdict(int)
        for number in nums:
            count_map[number] += 1

        res = []
        for number, occurrences in count_map.items():
            if occurrences >= threshold:
                res.append(number)
        
        return res