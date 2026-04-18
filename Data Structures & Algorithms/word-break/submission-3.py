class Trie:
    def __init__(self):
        self.is_word=False
        self.children=[None] * 26

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        memo={}
        def back(i):
            if i==len(s):
                return True
            if i in memo:
                return memo[i]

            curr=root
            

            for j in range(i, len(s)):
                ind= ord(s[j])- ord('a')
                
                if curr.children[ind]:
                    curr= curr.children[ind]
                else:
                    break
                if curr.is_word:
                    if back(j+1 ):
                        memo[i]=True
                        return True
                        
            memo[i]=False
            return False

        root = Trie()
        for word in wordDict:
            curr= root
            for w in word:
                ind = ord(w) - ord('a')
                if not curr.children[ind]:
                    curr.children[ind] = Trie()
                curr=curr.children[ind]
            curr.is_word=True
        
                



        return back(0)

        