class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap ={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res=[]

        def back(curr, i):
            if len(curr) == len(digits):
                res.append(curr)
                return
            

            for j in hmap[digits[i]]:
                back(curr+j, i+1)

        
        if digits:
            back("", 0)
        return res