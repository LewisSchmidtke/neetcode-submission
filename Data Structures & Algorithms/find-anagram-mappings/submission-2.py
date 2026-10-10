class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        
        for idx, number in enumerate(nums2):
            mapping[number] = idx

        for idx, number in enumerate(nums1):
            nums1[idx] = mapping[number]

        return nums1
        