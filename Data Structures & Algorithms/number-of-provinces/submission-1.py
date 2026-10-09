class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nr_of_connections = 0
        nr_of_cities = len(isConnected)

        for row in range(1, len(isConnected)):
            for col in range(row):
                if isConnected[row][col] == 1:
                    nr_of_connections += 1

        return nr_of_cities - nr_of_connections if nr_of_connections != nr_of_cities else 1