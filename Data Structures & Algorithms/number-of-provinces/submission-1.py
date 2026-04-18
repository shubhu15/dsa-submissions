class UnionFind:

    def __init__(self, size):
        self.parent = list(range(size))
        self.rank =[1]*size
        self.conn=size
    
    def find(self,x):
        if x!= self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parx = self.find(x)
        pary = self.find(y)

        if parx != pary:
            self.conn-=1
            if self.rank[parx]>self.rank[pary]:
                self.parent[pary] = parx
            elif self.rank[pary]>self.rank[parx]:
                self.parent[parx] = pary
            else:
                self.parent[parx]=pary
                self.rank[parx]+=1



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        # uf = UnionFind(n)

        # for i in range(n):
        #     for j in range(n):
        #         if ionnected[i][j]==1:
        #             uf.union(i,j)
        # return uf.connsC
        def dfs(i):
            if i>=n:
                return
            visited.add(i)
            for ne in range(n):
                if isConnected[i][ne]==1 and ne not in visited:
                    dfs(ne)

        


        visited = set()
        citi =0
        for i in range(n):
            if i not in visited:
                dfs(i)
                citi+=1
        return citi


