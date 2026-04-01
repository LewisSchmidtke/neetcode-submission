class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}

        for index2, n2 in enumerate(nums2):
            hashmap[n2] = index2
        
        for index1, n1 in enumerate(nums1):
            nums1[index1] = hashmap[n1]

        return nums1