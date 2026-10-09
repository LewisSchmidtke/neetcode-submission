class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placable_flowers = 0

        prev = None
        for index in range(len(flowerbed) - 1):
            if (prev is None or prev == 0) and flowerbed[index + 1] == 0 and flowerbed[index] == 0:
                flowerbed[index] = 1
                placable_flowers += 1

            prev = flowerbed[index]

        return n <= placable_flowers