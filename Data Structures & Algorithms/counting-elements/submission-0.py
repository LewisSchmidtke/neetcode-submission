class Solution:
    def countElements(self, arr: List[int]) -> int:
        track = set()
        counter = 0

        for num in arr:
            track.add(num + 1)

            if num in track:
                counter += 1

        return counter