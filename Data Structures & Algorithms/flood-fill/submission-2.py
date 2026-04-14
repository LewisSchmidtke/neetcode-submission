class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.starting_value = image[sr][sc]
        self.color = color
        self.image = image

        self.WIDTH = len(image)
        self.HEIGHT = len(image[0])
        self.seen = set()

        self.traverse(sr, sc)

        return self.image

    def traverse(self, r, c):
        if min(r,c) < 0 or r >= self.WIDTH or c >= self.HEIGHT:
            return

        if self.image[r][c] != self.starting_value:
            return

        if (r, c) in self.seen:
            return
        
        self.seen.add((r,c))
        self.image[r][c] = self.color

        self.traverse(r - 1, c) # up
        self.traverse(r, c + 1) # right
        self.traverse(r + 1, c) # down
        self.traverse(r, c - 1) # left