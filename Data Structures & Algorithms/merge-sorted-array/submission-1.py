class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Merge nums 1 ascending with nums 2 descending from nums1[m:]
        n1_pointer = m
        n2_pointer = 0

        while n1_pointer < len(nums1) and n2_pointer < len(nums2):
            nums1[n1_pointer] = nums2[n2_pointer]
            n1_pointer += 1
            n2_pointer += 1

        nums1.sort()
                
       

        