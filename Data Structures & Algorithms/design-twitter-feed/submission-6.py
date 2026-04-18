class Twitter:

    def __init__(self):

        self.follow_map=defaultdict(set)
        self.tweets =defaultdict(list)
        self.time=-1
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.time+=1
        self.tweets[userId].append((tweetId, self.time))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweets[userId][:] 
        for f in self.follow_map[userId]:
            feed.extend(self.tweets[f])
        feed.sort(key= lambda x: -x[1])
        return [ids for ids, _ in feed[:10] ]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.follow_map[followerId].discard(followeeId)
        
