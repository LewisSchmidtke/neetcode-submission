class Solution:
    def countElements(self, arr: List[int]) -> int:
        track = set()
        counter = 0

        arr.sort(reverse = True)
        print(arr)

        for num in arr:
            track.add(num)

            if num + 1 in track:
                counter += 1


        return counter