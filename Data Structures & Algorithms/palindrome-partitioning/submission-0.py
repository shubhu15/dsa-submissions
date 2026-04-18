class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalin(strg):
            a= 0
            b= len(strg)-1
            while a<=b:
                if strg[b]!=strg[a]:
                    return False
                a+=1
                b-=1
            return True
        
        res=[]

        def back(curr,i):
            if i==len(s):
                res.append(curr[:])
                return
            
            for j in range(i, len(s)):
                subs = s[i:j+1]

                if isPalin(subs):
                    curr.append(subs)
                    back(curr, j+1)
                    curr.pop()

        back([],0)

        return res



        