class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        res=[]

        def back(curr, i):
            res.append(curr[:])
            for j in range(i, len(nums)):
                curr.append(nums[j])
                back(curr, j+1)
                curr.pop()

        back([],0)
        print(res)
        sumx=0

        for r in res:
            if len(r)>1:
                xo=0
                for s in r:
                    xo = xo ^ s
                sumx+=xo
            else:
                sumx += 0 if len(r)==0 else r[0]

        return sumx
        