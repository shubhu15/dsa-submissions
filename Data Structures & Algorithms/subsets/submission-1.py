class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def subset(curr, i):
            res.append(curr[:])
            for j in range(i, len(nums)):
                curr.append(nums[j])
                subset(curr, j+1)
                curr.pop()

        subset([],0)
        return res
                

        