import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.timer = 1
        self.userTweetList = dict()
        self.followList = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userTweetList:
            tweetList = []
            tweetList.append((self.timer, tweetId))
            self.userTweetList[userId] = tweetList
        else:
            self.userTweetList[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        heapq.heapify(minheap)

        if userId in self.userTweetList:
            for i in range(len(self.userTweetList[userId])):
                heapq.heappush(minheap, self.userTweetList[userId][i])
                if len(minheap) > 10:
                    heapq.heappop(minheap)
        
        if userId in self.followList:
            for following in self.followList[userId]:
                if following in self.userTweetList:
                    for i in range(len(self.userTweetList[following])):
                        heapq.heappush(minheap, self.userTweetList[following][i])
                        if len(minheap) > 10:
                            heapq.heappop(minheap)
        
        feed = []
        while len(minheap) > 0:
            tweet = heapq.heappop(minheap)
            feed.append(tweet[1])
        feed.reverse()
        return feed
                
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followList:
            myFollowList = set()
            myFollowList.add(followeeId)
            self.followList[followerId] = myFollowList
        else:
            self.followList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followList:
            if followeeId in self.followList[followerId]:
                self.followList[followerId].remove(followeeId)
        
'''
postTweet creates a new tweet with tweetID and userID (need unique tweetID)
getNewsFeed retrieves the 10 most recent tweetIDs in the user's news feed
follow makes followerID follow followeeID
unfollow makes followerID unfollow followeeID

postTweet
    - keep track of a timer that is incremented every time a new tweet is posted
    - each user maintains their own list of tweets
    - maintain a map where key is userID and value is their list of tweets

follow and unfollow:
    - maintain a map where key is userID and value is list of users that they are following

getNewsFeed
    - maintain a minheap of size 10 -> O(1) insert and pop
    - iterate through the tweet list of all following and add to heap if greater than smallest item in heap
    - pop 10 items from the heap and return that as answer

'''

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)