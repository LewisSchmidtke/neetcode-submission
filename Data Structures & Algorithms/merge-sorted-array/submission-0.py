class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Merge nums 1 ascending with nums 2 descending from nums1[m:]
        mrge = m
        n2_pointer = n - 1

        while mrge < m + n:
            nums1[mrge] = nums2[n2_pointer]
            mrge += 1
            n2_pointer -= 1
        
        # 3 pointer approach to sort in place
        p1 = 0
        p2_back = m + n - 1
        p3_comp = p2_back - 1

        while p1 < m + n - 1:
            if nums1[p1] > nums1[p2_back]:
                nums1[p1], nums1[p2_back] = nums1[p2_back], nums1[p1] # We flip
                if nums1[p2_back] > nums1[p3_comp] and p1 < m + n - 2: # Exclude last 2 elements
                    nums1[p2_back], nums1[p3_comp] = nums1[p3_comp], nums1[p2_back] # We flip back end
                
            p1 += 1
        