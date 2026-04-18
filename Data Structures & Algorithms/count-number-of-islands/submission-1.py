class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n= len(grid[0])
        dirc = [ (1,0), (0,1), (-1, 0), (0,-1)]

        # def dfs(i,j):
        #     if i<0 or j<0 or i>=m or j >=n or grid[i][j]=='0':
        #         return
        #     grid[i][j]='0'
        #     dfs(i+1, j)
        #     dfs(i,j+1)
        #     dfs(i-1, j)
        #     dfs(i, j-1)
        def bfs(i,j):
            que = deque([(i,j)])
            grid[i][j]='0'
            while que:
                x,y = que.popleft()
                for dr, dc in dirc:
                    
                    if 0<=x+dr<m and 0<=y+dc<n and grid[x+dr][y+dc]!='0':
                        grid[dr+x][dc+y]='0'
                        que.append((dr+x, dc+y))




        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    cnt+=1
                    bfs(i,j)
        return cnt

        