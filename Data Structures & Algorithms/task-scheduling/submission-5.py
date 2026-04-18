class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        heap =[]
        count = Counter(tasks)
        for k,v in count.items():
            heapq.heappush(heap, -v)

        que= deque()
        time=0
        while heap or que:
            time+=1
            if not heap:
                time = que[0][0]
            else :
                cnt = heapq.heappop(heap) +1
                if cnt: 
                    que.append([ time+n, cnt])

            if que and que[0][0]==time:
                t, freq= que.popleft()
                heapq.heappush(heap, freq)
        return time

