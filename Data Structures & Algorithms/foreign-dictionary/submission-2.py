class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj= defaultdict(set)
        indegree = {}
        for w in words:
            for c in w:
                indegree[c]=0

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            minl = min(len(w1), len(w2) )
            if len(w1)>len(w2) and w1[:minl]==w2[:minl]:
                return ""

            for j in range(minl):
                if w1[j]!= w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]]+=1
                    break
        que= deque()
        for i, j in indegree.items():
            if j==0:
                que.append(i)
        res=[]

        while que:
            ch = que.popleft()
            res.append(ch)
            for ne in adj[ch]:
                indegree[ne]-=1
                if indegree[ne]==0:
                    que.append(ne)
        if len(res) < len(indegree):
            return ""

        return "".join(res)


            


        