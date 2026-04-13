from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = [] 
        self.tweet_counter = 0    

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((self.tweet_counter, tweetId, userId))
        self.tweet_counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = self.tweets[:]
        heapq.heapify_max(max_heap)

        res = []
        seen = []

        while len(res) < 10 and len(max_heap) > 0:
            tweet = heapq.heappop_max(max_heap)
            recent, post, user = tweet[0], tweet[1], tweet[2]
            if user != userId and user not in self.followers[userId]:
                seen.append((post, user))
            else:
                res.append(post)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
