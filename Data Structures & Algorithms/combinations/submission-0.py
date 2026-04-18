class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        nums = list(range(1,n+1))

        res=[]

        def back(i,curr):
            if len(curr)==k:
                res.append(curr[:])
                return

            for j in range(i,len(nums)):
                curr.append(nums[j])
                back(j+1, curr)
                curr.pop()

        back(0, [])
        return res
        