class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        pac = set()
        alt = set()

        def dfs(i,j, visit, prev):
            if (i,j) in visit or i<0 or j<0 or i>=row or j>=col or heights[i][j]<prev:
                return

            visit.add((i,j))
            dfs(i+1, j, visit, heights[i][j])
            dfs(i, j+1, visit, heights[i][j])
            dfs(i-1, j, visit, heights[i][j])
            dfs(i, j-1, visit, heights[i][j])

        
        for i in range(row):
            dfs(i,0, pac, heights[i][0])
            dfs(i, col-1, alt, heights[i][col-1])

        for j in range(col):
            dfs(0,j, pac, heights[0][j])
            dfs(row-1, j , alt, heights[row-1][j])
        
        res=[]
        for i in range(row):
            for j in range(col):
                if (i,j) in pac and (i,j) in alt:
                    res.append([i,j])
        return res




        