class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        state=0
        min_x= float("inf")
        i=0

        for j in range(len(nums)):
            state+=nums[j]

            while state>= target:
                min_x = min(min_x, j-i+1)
                state-=nums[i]
                i+=1

        return 0 if min_x==float("inf") else min_x
        