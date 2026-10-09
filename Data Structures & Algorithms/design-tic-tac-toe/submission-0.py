class TicTacToe:

    def __init__(self, n: int):
        self.grid = [[0] * n] * n
        self.h_sum = [0] * n
        self.v_sum = [0] * n
        self.n = n


    def move(self, row: int, col: int, player: int) -> int:
        self.grid[row][col] = player

        if player == 2:
            val = self.n + 1
        else:
            val = 1

        self.h_sum[row] += val
        self.v_sum[col] += val
        d_sum = sum([self.grid[k][k] for k in range(self.n)])

        if self.h_sum[row] / self.n == val or self.v_sum[col] / self.n == val or d_sum / self.n == val:
            if val == self.n + 1:
                return 2

            return 1

        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
