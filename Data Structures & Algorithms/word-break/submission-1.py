class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordD = set(wordDict)
        memo={}
        def back(i):
            if i==len(s):
                return True
            if i in memo:
                return memo[i]
            st=""

            for j in range(i, len(s)):
                st +=s[j]
                if st in wordDict:
                    if back(j+1):
                        memo[i]=True
                        return True
            memo[i]=False
            return False


        return back(0)

        