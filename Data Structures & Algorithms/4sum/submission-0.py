class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:


        nums.sort()

        res=set()

        for i in range(len(nums)):
            a = nums[i]
            for j in range(i+1, len(nums)):
                b= nums[j]

                k=j+1
                l= len(nums)-1
                while k<l:
                    t = a+b+nums[k]+nums[l]
                    if t== target:
                        res.add((a,b,nums[k],nums[l]))
                        k+=1
                        l-=1
                    elif t>target:
                        l-=1
                    else:
                        k+=1

        return list(res)


        
        