class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        def back(curr, i):
            res.append(curr[:])
                
            
            
            for j in range(i, len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                curr.append(nums[j])
                back(curr, j+1)
                curr.pop()

        back([],0)
        return res

        