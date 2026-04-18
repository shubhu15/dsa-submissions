class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs =nums[0]
        currs = 0
        for i in nums:
            currs+=i
            maxs = max(currs, maxs)
            if currs<0:
                currs=0
        return maxs
        