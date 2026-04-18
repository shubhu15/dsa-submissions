class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        fresh=0
        que= deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    que.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        time=0
        dirc = [(1,0), (0,1), (-1,0), (0,-1)]
        while que and fresh>0:
            l = len(que)
            for i in range(l):
                r,c = que.popleft()
                for dr, dc in dirc:
                    nr = r+dr
                    nc = c+dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                        fresh-=1
                        que.append((nr, nc))
                        grid[nr][nc]=2
            time+=1

        if fresh>0:
            return -1

        return time
