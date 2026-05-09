class HitCounter:

    def __init__(self):
        self.queue = deque()
        self.max_window = 300

        

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        cutoff = timestamp - self.max_window

        while self.queue and self.queue[0] <= cutoff:
            self.queue.popleft()
        
        return len(self.queue)

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
