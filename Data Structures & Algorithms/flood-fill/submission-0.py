class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.starting_value = image[sr][sc]
        self.color = color
        self.image = image

        self.WIDTH = len(image)
        self.HEIGHT = len(image[0])

        self.traverse(sr, sc)

        return self.image

    def traverse(self, r, c):
        if min(r,c) < 0 or max(r,c) >= self.WIDTH or max(r,c) >= self.HEIGHT:
            return

        if self.image[r][c] != self.starting_value:
            return

        self.traverse(r, c)
        self.traverse(r, c)
        self.traverse(r, c)