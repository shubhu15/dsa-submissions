class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums[0]<=nums[-1]:
            return nums[0]

        i=0
        j=len(nums)-1
        while i<=j:
            mid = i + (j-i)//2
            print(mid)
            if nums[mid]<nums[j]:
                j=mid
            else:
                i=mid+1
            
        return nums[i-1]


