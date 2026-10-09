class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        width = len(picture)
        height = len(picture[0])

        width_arr = [0] * width
        height_arr = [0] * height

        for w in range(width):
            for h in range(height):
                if picture[w][h] == "B":
                    width_arr[w] += 1
                    height_arr[h] += 1

        lonely_pixels = 0

        for w in range(width):
            for h in range(height):
                if picture[w][h] == "B" and width_arr[w] == 1 and height_arr[h] == 1:
                    lonely_pixels += 1

        return lonely_pixels