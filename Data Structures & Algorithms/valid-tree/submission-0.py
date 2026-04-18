class UnionFind:

    def __init__(self,n):
        self.root= list(range(n+1))
        self.comp=n
    def find(self,x):
        if self.root[x]!=x:
            self.root[x]= self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        parx = self.find(x)
        pary = self.find(y)
        if parx== pary:
            return False
        self.comp-=1
        self.root[parx]= pary
        return True



class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n-1:
            return False
        uf = UnionFind(n)
        for u,v in edges:
            if not uf.union(u,v):
                return False
        return uf.comp==1

        