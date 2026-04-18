class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree =[0]*numCourses
        adjmap = defaultdict(list)
        for i,j in prerequisites:
            indegree[j]+=1
            adjmap[i].append(j)

        
        # que= deque()
        # for i in range(len(indegree)):
        #     if indegree[i] ==0:
        #         que.append(i)
        
        # res=[]
        # while que:
        #     cr = que.popleft()
        #     res.append(cr)
        #     for l in adjmap[cr]:
        #         indegree[l]-=1
        #         if indegree[l]==0:
        #             que.append(l)

        # return res[::-1] if len(res)== numCourses else []

        res=[]
        visited = set()
        visiting =set()

        def dfs(curr):
            if curr in visited:
                return True
            if curr in visiting:
                return False

            visiting.add(curr)
            for ad in adjmap[curr]:
                if not dfs(ad):
                    return False
            visiting.remove(curr)
            visited.add(curr)
            res.append(curr)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res