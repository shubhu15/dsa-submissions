class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        adj=defaultdict(list)

        for fl in flights:
            adj[fl[0]].append((fl[1], fl[2]))

        dist = [ float("inf")]*(n)
        dist[src]=0
        que= deque()

        que.append((src, 0, 0))
        minc = float("inf")

        while que:
            point, price, stop = que.popleft()

            if stop<=k+1 and point==dst:
                minc = min(minc, price)
            
            for ne, cost in adj[point]:
                if cost+price<dist[ne]:
                    dist[ne]=cost+price
                    que.append((ne, cost+price, stop+1))
        return minc if minc!=float("inf") else -1
