class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree =[0]*numCourses
        adjmap = defaultdict(list)
        for i,j in prerequisites:
            indegree[j]+=1
            adjmap[i].append(j)

        
        que= deque()
        for i in range(len(indegree)):
            if indegree[i] ==0:
                que.append(i)
        
        num =0
        while que:
            cr = que.popleft()
            num+=1
            for l in adjmap[cr]:
                indegree[l]-=1
                if indegree[l]==0:
                    que.append(l)

        return True if num== numCourses else False


        

        