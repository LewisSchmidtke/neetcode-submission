class Leaderboard:

    def __init__(self):
        self.score_board = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.score_board:
            self.score_board[playerId] = score
        else:
            self.score_board[playerId] += score        

    def top(self, K: int) -> int:
        scores = sorted(list(self.score_board.values()), reverse=True)
        return sum(scores[:K])

    def reset(self, playerId: int) -> None:
        self.score_board.pop(playerId)
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
