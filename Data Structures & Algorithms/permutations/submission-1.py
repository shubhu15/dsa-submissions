class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def back(nums,s):
            if s==len(nums):
                res.append(nums[:])
                return
            
            for i in range(s,len(nums)):
                nums[i], nums[s]= nums[s], nums[i]
                back(nums, s+1)
                nums[i], nums[s]= nums[s], nums[i]
                

        back(nums, 0)
        return res
        