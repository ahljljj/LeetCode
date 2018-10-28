"""
355. Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);



"""


'''
wrong

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.posts = {}
        self.myposts = {}
        self.friends = {}
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.posts:
            self.posts[userId] = [tweetId]
        else:
            self.posts[userId].append(tweetId)
            
        if userId not in self.myposts:
            self.myposts[userId] = [tweetId]
        else:
            self.myposts[userId].append(tweetId)
            
        if userId in self.friends:
            for follower in self.friends[userId]:
                self.posts[follower].append(tweetId)            
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.posts:
            self.posts[userId] = []
            return self.posts[userId]
        
        return self.posts[userId][::-1][:10]
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        # key: followee value: follower  followerId not in self.friends[followeeId]
        if followerId != followeeId:
            if followeeId not in self.friends:
                self.friends[followeeId] = [followerId]
            elif followerId in self.friends[followeeId]:
                return
            else:
                self.friends[followeeId].append(followerId)
            
            if followerId not in self.posts:
                self.posts[followerId] = []
            if followeeId not in self.posts:
                self.posts[followeeId] = []
            self.posts[followerId].extend(self.posts[followeeId])
            
                    

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId  and followeeId in self.friends:
            if followerId in self.friends[followeeId]:
                for post in self.myposts[followeeId]:
                    if post in self.posts[followerId]:
                        self.posts[followerId].remove(post)
                self.friends[followeeId].remove(followerId)
            
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
'''