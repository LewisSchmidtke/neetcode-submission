class Solution:
    def isPathCrossing(self, path: str) -> bool:
        grid = set()
        location = (0, 0)
        grid.add(location)

        directions = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0),
        }

        for direction in path:
            curr_x, curr_y = location[0], location[1]  
            location = (directions[direction][0] + curr_x, directions[direction][1] + curr_y)
            if location in grid:
                return True
            grid.add(location)
        
        return False

