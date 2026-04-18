class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        

        def back(curr, res,opend, closed):
            if opend==closed==n and len(curr)==2*n:
                res.append(str(curr))
                return
            
            if closed<opend:
                 back(curr+')', res,opend, closed+1)
            if opend<n:
                 back(curr+'(', res,opend+1, closed)

        back('', res, 0,0)
        return res


