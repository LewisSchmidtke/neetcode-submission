class Solution:
    def countElements(self, arr: List[int]) -> int:
        track = set(arr)
        counter = 0

        for num in arr:
            if num + 1 in track:
                counter += 1


        return counter