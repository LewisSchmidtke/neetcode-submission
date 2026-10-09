class TicTacToe:

    def __init__(self, n: int):
        self.h_sum = [0] * n
        self.v_sum = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n


    def move(self, row: int, col: int, player: int) -> int:
        if player == 2:
            val = self.n + 1
        else:
            val = 1

        self.h_sum[row] += val
        self.v_sum[col] += val

        if row == col:
            self.diag += val
        
        if row + col == self.n - 1:
            self.anti_diag += val

        if self.h_sum[row] / self.n == val or self.v_sum[col] / self.n == val or self.diag / self.n == val or self.anti_diag / self.n == val:
            if val == self.n + 1:
                return 2

            return 1

        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
