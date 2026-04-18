class Solution:
    def minWindow(self, s: str, t: str) -> str:

        mapt = Counter(t)
        want= len(mapt)
        has=0
        maps=defaultdict(int)
        if len(s)<len(t):
            return ""

        i=0
        resl=float("infinity")
        res=""
        j=0
        while j<len(s):
            maps[s[j]]+=1

            if s[j] in mapt and maps[s[j]]== mapt[s[j]]:
                has+=1
            
            while has==want:
                print(res)
                if j-i+1<=resl:
                    resl = j-i+1
                    res = s[i:j+1]
                
                
                if s[i] in mapt and maps[s[i]]==mapt[s[i]]:
                    has-=1
                maps[s[i]]-=1
                i+=1
            j+=1

       
        return res




        