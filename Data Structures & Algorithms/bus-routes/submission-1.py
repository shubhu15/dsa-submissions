class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:


        adj = defaultdict(list)


        for i, r in enumerate(routes):
            for s in r:
                adj[s].append(i)

        visited= set()
        if source == target:
            return 0
        que= deque()
        
        for s in adj[source]:
            que.append((s,1))
            visited.add(s)

        while que:
            route, cost = que.popleft()
            if route in adj[target]:
                return cost
            
            for stop in routes[route]:
                for r in adj[stop]:
                    if r not in visited:
                        que.append((r,cost+1))
                        visited.add(r)

        return -1

        