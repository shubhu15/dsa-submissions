class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        row = len(grid)
        col = len(grid[0])
        que= deque()
        dirc =[(1,0),(0,1),(-1,0), (0,-1)]
        visited= set()

        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    que.append((i,j,0))
        dis=0
        
        while que:
            r,c,dis= que.popleft()
            
            for x,y in dirc:
                dr= r+x
                dc= c+y
                if 0<=dr<row and 0<=dc<col and grid[dr][dc]>0 and (dr,dc) not in visited:
                    grid[dr][dc]=dis+1
                    visited.add((dr,dc))
                    que.append((dr,dc, dis+1))

        



        
        