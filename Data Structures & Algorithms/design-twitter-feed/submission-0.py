from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = []     

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = self.tweets[:]
        heapq.heapify_max(max_heap)

        res = []
        seen = []

        while len(res) <= 10 and len(max_heap) > 0:
            tweet = heapq.heappop_max(max_heap)
            post, user = tweet[0], tweet[1]
            if user != userId and user not in self.followers[userId]:
                seen.append((post, user))
            else:
                res.append(post)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
