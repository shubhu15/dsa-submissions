class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        res=0
        l=0
        pdt=1
        for r in range(len(nums)):
            pdt *= nums[r]

            while l<=r and pdt>=k:
                pdt = pdt//nums[l]
                l+=1

            res += (r-l+1)
            
        return res
        