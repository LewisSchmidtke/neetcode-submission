class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        min_tick = tickets[k]
        time = 0

        for idx, tick in enumerate(tickets):
            if idx < k:
                time += min(min_tick, tick) # If tick larger min_tick will need more queue iterations, not relev.
            elif idx > k:
                time += min(min_tick - 1, tick) # Will see 1 less queue iteration so -1
            else: # idx == k
                time += min_tick
        
        return time
