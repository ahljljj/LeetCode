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


# hashtable, heap


'''
intuition

OOD design:
data structure need in the Tweet system:

1. A data structure that save the following relationship
2. A data structure that save the tweets posted 
Based on the requirement of method 3: we should get our followees' tweets and select the most recent 10 tweet. So there should have a timestamp inside the tweet. So we create a new class to represent a tweet

3. A class Tweet containing timestamp
There are some tips in the system:

1. One should get the tweets of itself, which means the followee must contain itself
2. Since the followee must contains itself, it cannot unfollow itself(unfollow add this constraint)
3. The followees must be identical
According to the analysis above, we have these data struture in this class:

1. A HashMap(follower, Set(followees))
2. A HashMap(UserId, List(Tweet))
3. A Static int timeStamp
4. A int Maximum number of feed(can adjust if needed, optional)


'''


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxnews = 10
        self.time = 0
        self.posts = {}  # key: userId, val: list of pairs (time, post)
        self.friends = {}  # key: follower val: set of followee

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.time += 1
        self.posts[userId] = self.posts.get(userId, []) + [[self.time, tweetId]]

    def getNewsFeed(self, userId): #time complexity O(nlgk)
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        self.posts[userId] = self.posts.get(userId, [])
        self.friends[userId] = self.friends.get(userId, set())
        news = []
        posts = self.posts[userId][:]

        for followee in self.friends[userId]:
            posts.extend(self.posts.get(followee, []))

        heapq.heapify(news)  # min heap
        count = 0
        for (time, post) in posts:
            count += 1
            if count > self.maxnews:
                if time > news[0][0]:
                    heapq.heappop(news)
                    heapq.heappush(news, [time, post])
            else:
                heapq.heappush(news, [time, post])
        res = []
        while news:
            res.append(heapq.heappop(news)[1])
        return res[::-1]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self.friends[followerId] = self.friends.get(followerId, set()) | set([followeeId])

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self.friends[followerId] = self.friends.get(followerId, set())
            if followeeId in self.friends[followerId]:
                self.friends[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)