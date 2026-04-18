class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+ "#"+s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        num=0
        i=0
        while i<len(s):
            while s[i]!="#":
                num = num*10 + int(s[i])
                i+=1
            
            r=""
            if i+1<len(s):
                r = s[i+1: i+num+1]
            res.append(r)
            
            i+=num+1
            num=0
        return res






        return res
