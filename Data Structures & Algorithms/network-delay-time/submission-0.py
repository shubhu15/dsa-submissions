class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        adj = defaultdict(list)
        for time in times:
            v=time[0]
            u=time[1]
            t=time[2]
            adj[v].append((u,t))

        visited = set()
        dis =[ float("inf")]*(n+1)
        dis[k]=0
        heap = [(0,k)]
        while heap:
            dist, s = heapq.heappop(heap)
            if s in visited:
                continue
            visited.add(s)

            for u,t in adj[s]:
                if dist+t <dis[u]:
                    dis[u]= dist+t
                    heapq.heappush(heap, (dist+t, u))

        maxd = max(dis[1:])
        return maxd if maxd!=float("inf") else -1