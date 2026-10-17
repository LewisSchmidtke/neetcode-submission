class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []

        a1 = a2 = a3 = 0

        while a1 < len(arr1) and a2 < len(arr2) and a3 < len(arr3):
            if arr1[a1] == arr2[a2] == arr3[a3]:
                res.append(arr1[a1])
                a1 += 1
                a2 += 1
                a3 += 1
            else:
                mini = min(arr1[a1], arr2[a2], arr3[a3])
                if arr1[a1] == mini: a1 += 1
                if arr2[a2] == mini: a2 += 1
                if arr3[a3] == mini: a3 += 1

        return res
        