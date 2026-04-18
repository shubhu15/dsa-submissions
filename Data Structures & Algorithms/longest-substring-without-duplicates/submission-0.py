class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        l=0
        hmap=set()
        res=0
        for r in range(len(s)):
            
            
            while hmap and s[r] in hmap:
                hmap.remove(s[l])
                l+=1
            hmap.add(s[r])
                
            res= max(res, r-l+1)
        return res

