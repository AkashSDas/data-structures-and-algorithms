from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.followings: dict[int, set[int]] = defaultdict(set)
        self.tweets: dict[int, list[tuple[int, int]]] = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1

        self.tweets[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        followees = self.followings[userId]
        tweets: dict[int, int] = {}  # count:tweet
        max_heap: list[int] = []

        for followee_user_id in [*followees, userId]:
            for tweet in self.tweets[followee_user_id]:
                tweets[-tweet[0]] = tweet[1]
                max_heap.append(-tweet[0])

        heapq.heapify(max_heap)

        result: list[int] = []

        for _ in range(min(len(tweets), 10)):
            count = heapq.heappop(max_heap)
            result.append(tweets[count])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].discard(followeeId)
