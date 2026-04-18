class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxp = max(count.values())

        res=0
        for i,j in count.items():
            if j == maxp:
                res+=1

        return max(res + (n+1)*(maxp-1) , len(tasks))     