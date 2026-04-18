class Twitter:

    def __init__(self):

        self.follow_map=defaultdict(set)
        self.tweets =defaultdict(list)
        self.time=-1
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.time+=1
        self.tweets[userId].append((tweetId, self.time))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # feed = self.tweets[userId][:] 
        # for f in self.follow_map[userId]:
        #     feed.extend(self.tweets[f])
        # feed.sort(key= lambda x: -x[1])
        # return [ids for ids, _ in feed[:10] ]
        minheap=[]
        self.follow_map[userId].add(userId)

        for follower in self.follow_map[userId]:
            if follower in self.tweets:
                ind = len(self.tweets[follower])-1
                tweetid, cnt = self.tweets[follower][ind]
                heapq.heappush(minheap, (-cnt, tweetid, follower, ind-1))

        res=[]
        while minheap and len(res)<10:
            cnt, tweetid, follower, ind = heapq.heappop(minheap)
            res.append(tweetid)
            if ind>=0:
                tweetid, cnt = self.tweets[follower][ind]
                heapq.heappush(minheap, (-cnt, tweetid, follower, ind-1))

        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.follow_map[followerId].discard(followeeId)
        
