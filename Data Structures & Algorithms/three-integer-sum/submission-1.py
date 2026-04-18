class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        i=0
        res=[]
        nums= sorted(nums)

        res=set()

        for i in range(len(nums)):
            n1= nums[i]
            j=i+1
            k= len(nums)-1
            while j<k:
                target = n1 + nums[j]+nums[k]
                if target==0:
                    res.add((n1, nums[j], nums[k]))
                    k-=1
                    j+=1
                    # break
                elif target>0:
                    k-=1
                else:
                    j+=1

        return list(res)

        