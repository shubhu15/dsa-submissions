class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def subset(curr, i):
            if i== len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            subset(curr,i+1)
            curr.pop()
            subset(curr, i+1)

        subset([],0)
        return res
                

        