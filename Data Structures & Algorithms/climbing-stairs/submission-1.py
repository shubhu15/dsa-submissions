class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def dfs(r):
            if r>n:
                return 0
            if r==n:
                
                return 1
            if r in dp:
                return dp[r]
            dp[r] = dfs(r+1) + dfs(r+2)
            return dp[r]
        
        return dfs(0)
