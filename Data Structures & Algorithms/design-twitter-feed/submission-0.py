import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet_map = defaultdict(list)    # userId -> list of (time, tweetId)
        self.follow_map = defaultdict(set)   # followerId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet_map[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = []
        max_heap = []

        # Feed includes followees and the user's own tweets
        sources = self.follow_map[userId] | {userId}

        # Initialize the heap with each source's most recent tweet
        for source_id in sources:
            tweets = self.tweet_map[source_id]
            if tweets:
                idx = len(tweets) - 1
                time, tweet_id = tweets[idx]
                # Store -time to simulate a max-heap with Python's min-heap
                max_heap.append((-time, tweet_id, source_id, idx))

        heapq.heapify(max_heap)

        # Merge up to 10 most recent tweets
        while max_heap and len(feed) < 10:
            _, tweet_id, source_id, idx = heapq.heappop(max_heap)
            feed.append(tweet_id)
            
            # Push the next most recent tweet from the same source
            if idx > 0:
                prev_time, prev_tweet_id = self.tweet_map[source_id][idx - 1]
                heapq.heappush(max_heap, (-prev_time, prev_tweet_id, source_id, idx - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)