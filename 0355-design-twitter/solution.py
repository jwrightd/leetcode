class Twitter(object):
    import heapq

    def __init__(self):
        self.counter = 0
        self.followers = {}
        self.tweets = {}

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId in self.tweets:
            self.tweets[userId].append((self.counter, tweetId)) # max heap so we can pop latest things
        else:
            self.tweets[userId] = [(self.counter, tweetId)]
        self.counter += 1
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        heap = []
        output = []
        # add userId and follower stuff
        if userId in self.tweets:
            for order, tid in self.tweets[userId]:
                heapq.heappush(heap, (order, tid))
                if len(heap) > 10:
                    heapq.heappop(heap)
        if userId in self.followers:
            for flwr in self.followers[userId]:
                if flwr in self.tweets:
                    for order, tid in self.tweets[flwr]:
                        heapq.heappush(heap, (order, tid))
                        if len(heap) > 10:
                            heapq.heappop(heap)
        while heap:
            order, tid = heapq.heappop(heap)
            output.append(tid)
        return output[::-1] #rev order





    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.followers:
            self.followers[followerId].add(followeeId)
        else:
            self.followers[followerId] = set()
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


# ok let's think about the DS we need

# im thinking size-10 PQ for getNewsFeed
# we need like adj list of followers (dictionary) --> user to followers
# dictionary for user --> tweets
# tweets stored with (counter, id)
# global counter for each event (0 to whatever)
