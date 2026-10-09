# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # Find person whose node has n - 1 pointers towards it
        adj_list = defaultdict(set)

        for src in range(n):
            for dest in range(n):
                if src == dest:
                    continue

                if knows(src, dest):
                    adj_list[dest].add(src) # Basically is known by
                    if len(adj_list[dest]) == n - 1:
                        return dest

        return -1
