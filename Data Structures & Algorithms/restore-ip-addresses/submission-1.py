class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res=[]

        def back(curr, i, dots):
            if dots==4 and i==len(s):
                res.append(".".join(curr[:]))
                return

            for j in range(1, 4):
                if i +j>len(s):
                    return
                subs = s[i:i+j]
                if int(subs)<=255 and (subs=='0' or not subs.startswith('0')):
                    curr.append(subs)
                    back(curr, i+j, dots+1)
                    curr.pop()

        back([], 0, 0)
        return res







            