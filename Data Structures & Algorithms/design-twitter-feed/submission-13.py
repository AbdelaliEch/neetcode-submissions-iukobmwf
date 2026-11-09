class Twitter:

    def __init__(self):
        self.posts_data = dict()
        self.followers_data = defaultdict(set)
        self.time = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.posts_data:
            self.posts_data[userId] = {"ownPosts": [], "followeesPosts": []}

        self.posts_data[userId]["ownPosts"].append((self.time, tweetId))
        for follower in self.followers_data[userId]:
            self.posts_data[follower]["followeesPosts"].append((self.time, tweetId))
        
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:

        if not userId in self.posts_data:
            self.posts_data[userId] = {"ownPosts": [], "followeesPosts": []}

        totalPosts = self.posts_data[userId]["ownPosts"] + self.posts_data[userId]["followeesPosts"]
        heapq.heapify(totalPosts)

        k = 10
        output = []
        while k > 0 and len(totalPosts):
            output.append(heapq.heappop(totalPosts)[1])
            k -= 1

        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.posts_data:
            self.posts_data[followeeId] = {"ownPosts": [], "followeesPosts": []}

        if followerId not in self.posts_data:
            self.posts_data[followerId] = {"ownPosts": [], "followeesPosts": []}

        if followerId not in self.followers_data[followeeId]:
            self.followers_data[followeeId].add(followerId)
            for post in self.posts_data[followeeId]["ownPosts"]:
                self.posts_data[followerId]["followeesPosts"].append(post)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers_data[followeeId]:
            self.followers_data[followeeId].remove(followerId)
            for post in self.posts_data[followeeId]["ownPosts"]:
                self.posts_data[followerId]["followeesPosts"].remove(post)
