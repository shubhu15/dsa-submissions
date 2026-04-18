class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        if row*col<len(word):
            return False
        visited = set()
        dirc =[(1,0), (0,1), (-1, 0), (0,-1)]
        f=[False]


        def dfs(r,c, i):
            
            if i==len(word):
                return True
            if r<0 or c<0 or r>=row or c>=col or word[i]!=board[r][c] or (r,c) in visited:
                return False
            visited.add((r,c))
            for x,y in dirc:
                dr, dc = x+r, y+c
                if (dr, dc) not in visited:
                    
                    f[0] = f[0] or dfs(dr, dc, i+1)
                        
            visited.remove((r, c))
            return f[0]

        for j in range(row):
            for k in range(col):
                if board[j][k]== word[0] and (j,k) not in visited:
                    if dfs(j,k,0):
                        return True

        return False
                    
            






        